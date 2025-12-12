-- Chat sessions for rate limiting and history
CREATE TABLE IF NOT EXISTS website_chat_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    visitor_id TEXT NOT NULL,  -- IP hash for privacy
    created_at TIMESTAMPTZ DEFAULT NOW(),
    message_count INTEGER DEFAULT 0,
    lead_submitted BOOLEAN DEFAULT FALSE
);

-- Index for rate limiting queries
CREATE INDEX IF NOT EXISTS idx_chat_sessions_visitor_date
ON website_chat_sessions(visitor_id, created_at);

-- Chat messages (for conversation history)
CREATE TABLE IF NOT EXISTS website_chat_messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES website_chat_sessions(id) ON DELETE CASCADE,
    role TEXT NOT NULL CHECK (role IN ('user', 'assistant')),
    content TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index for fetching messages by session
CREATE INDEX IF NOT EXISTS idx_chat_messages_session
ON website_chat_messages(session_id, created_at);

-- Rate limit check function
CREATE OR REPLACE FUNCTION check_daily_chat_limit(
    p_visitor_id TEXT,
    p_daily_limit INTEGER DEFAULT 20
)
RETURNS TABLE(allowed BOOLEAN, remaining INTEGER, session_id UUID) AS $$
DECLARE
    v_session_id UUID;
    v_count INTEGER;
BEGIN
    -- Count messages from today for this visitor
    SELECT COALESCE(SUM(message_count), 0) INTO v_count
    FROM website_chat_sessions
    WHERE visitor_id = p_visitor_id
      AND created_at >= CURRENT_DATE;

    -- Check if limit exceeded
    IF v_count >= p_daily_limit THEN
        RETURN QUERY SELECT FALSE, 0, NULL::UUID;
        RETURN;
    END IF;

    -- Create new session
    INSERT INTO website_chat_sessions (visitor_id)
    VALUES (p_visitor_id)
    RETURNING id INTO v_session_id;

    RETURN QUERY SELECT TRUE, (p_daily_limit - v_count - 1), v_session_id;
END;
$$ LANGUAGE plpgsql;

-- Function to increment message count
CREATE OR REPLACE FUNCTION increment_message_count(p_session_id UUID)
RETURNS void AS $$
BEGIN
    UPDATE website_chat_sessions
    SET message_count = message_count + 1
    WHERE id = p_session_id;
END;
$$ LANGUAGE plpgsql;

-- GIN index on document_rows for fast order lookups
CREATE INDEX IF NOT EXISTS idx_document_rows_jsonb
ON document_rows USING GIN (row_data jsonb_path_ops);
