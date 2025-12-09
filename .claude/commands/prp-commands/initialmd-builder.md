# INITIAL.md Generator Prompt

You are tasked with creating a comprehensive INITIAL.md file for the KLM dashboard project based on the entire chat history with Claude Code. The file should be created at `~/PRPs/INITIAL.md` following the exact same structure and style as `~/PRPs/INITIAL-EXAMPLE.md`.

## Context

Based on the chat history and project documentation, you need to synthesize all information about the project to create a proper INITIAL.md specification.

## Required Structure

Follow this exact structure from INITIAL-EXAMPLE.md:

1. **## FEATURE:**
   - 2-3 paragraph comprehensive description of what needs to be built
   - Include specific technical requirements
   - Reference existing components that should be copied or used
   - Mention specific files, folders, or configurations needed

2. **## TOOLS:**
   - List of specific tools with function signatures
   - Each tool should have: `tool_name(param: type) -> return_type`: Description
   - Focus on essential tools only (8-10 max)

3. **## DEPENDENCIES**
   - Required parameters and context
   - Database connections
   - External services
   - Configuration needs

4. **## SYSTEM PROMPT(S)**
   - Detailed agent behavior instructions
   - Numbered list of capabilities
   - Guidelines for tool usage
   - Response quality standards

5. **## EXAMPLES:**
   - Reference to existing examples in the codebase
   - Mention specific folders and their purposes

6. **## DOCUMENTATION:**
   - Links to official docs
   - Reference materials
   - Internal documentation references

7. **## OTHER CONSIDERATIONS:**
   - Best practices
   - Configuration guidelines
   - Testing requirements

## Content Guidelines

Based on the chat history and project structure:

- The project has three main components: backend_agent_api, backend_rag_pipeline, frontend
- Uses Pydantic AI with MCP support
- FastAPI with SSE streaming
- Supabase for database
- React/TypeScript frontend
- Already has RAG pipeline set up
- Uses Archon for task management

## Instructions

1. Analyze the entire chat history for technical details, requirements, and patterns
2. Reference the INITIAL-EXAMPLE.md file for style and structure
3. Create a realistic INITIAL.md that could be used to build this project
4. Include specific technical details gathered from the conversation
5. Make sure all paths, folder names, and technical specifications are accurate
6. The output should be a complete INITIAL.md file content

## Output Format

Provide the complete content of the INITIAL.md file that should be created. Do not include explanations - just the file content following the exact structure of the example.

Remember to:
- Keep the same formatting and style as INITIAL-EXAMPLE.md
- Include specific technical details from the chat history
- Make it practical and implementable
- Reference actual files and folders in the project