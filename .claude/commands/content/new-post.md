---
description: Generate a new blog post with proper frontmatter and structure
argument-hint: [title] [category] [author]
---

# New Blog Post: $1

**Category:** $2 (defaults to "general")
**Author:** $3 (defaults to current user)

## Post Generation

### 1. File Setup

Create a new post file with:
- **Filename:** `[date]-[slugified-title].md`
- **Location:** Identify blog posts directory (common: `_posts/`, `content/posts/`, `blog/`)
- **Date format:** YYYY-MM-DD

### 2. Frontmatter Template

Generate appropriate frontmatter based on static site generator:

**Jekyll/GitHub Pages:**
```yaml
---
layout: post
title: "$1"
date: [current datetime]
author: "$3"
categories: [$2]
tags: []
excerpt: "[auto-generate 150-160 char summary]"
featured_image: "/assets/images/[slug]/hero.jpg"
published: false
---
```

**Hugo:**
```yaml
---
title: "$1"
date: [current datetime]
draft: true
author: "$3"
categories: ["$2"]
tags: []
description: "[auto-generate meta description]"
images: ["/images/[slug]/hero.jpg"]
---
```

**Next.js/MDX:**
```yaml
---
title: '$1'
publishedAt: '[current datetime]'
summary: '[auto-generate summary]'
author: '$3'
category: '$2'
image: '/images/[slug]/hero.jpg'
---
```

### 3. Content Structure

Generate initial content structure:

```markdown
# $1

[Opening hook - compelling question or statement]

## Introduction

[2-3 paragraphs introducing the topic, why it matters, what readers will learn]

## Key Takeaways

- [Main point 1]
- [Main point 2]
- [Main point 3]

## [Main Section 1]

[Content with subheadings as needed]

### [Subsection if needed]

## [Main Section 2]

[Content with examples, code blocks, images as appropriate]

## [Main Section 3]

[Practical applications or examples]

## Conclusion

[Summarize key points, call to action, next steps]

## Further Reading

- [Related internal post 1]
- [Related internal post 2]
- [External resource]

---

*Have questions or feedback? [Contact link or social media]*
```

### 4. SEO Optimization

**Meta Tags to Include:**
- Title (50-60 characters)
- Description (150-160 characters)
- Open Graph tags
- Twitter Card tags
- Canonical URL

**Content Optimization:**
- Target keyword placement (title, H1, first paragraph)
- Related keywords throughout
- Internal linking opportunities
- External authoritative links
- Image alt text templates

### 5. Asset Preparation

**Create directories:**
- `/images/[slug]/` for post images
- `/assets/[slug]/` for downloadable resources

**Image templates needed:**
- Hero image (1200x630 for social sharing)
- In-post images with proper sizing
- Alt text for accessibility

### 6. Checklist Items

**Pre-publish Checklist:**
```markdown
## Pre-Publish Checklist

- [ ] Spell check completed
- [ ] Grammar review done
- [ ] Facts and claims verified
- [ ] Links tested
- [ ] Images optimized (<100KB each)
- [ ] Alt text added to all images
- [ ] Mobile preview checked
- [ ] SEO meta tags completed
- [ ] Categories and tags appropriate
- [ ] Published date correct
- [ ] Author attribution correct
- [ ] Social sharing image created
```

### 7. Publishing Workflow

**Next Steps:**
1. Review generated structure
2. Fill in content sections
3. Run `/seo-analyze` for optimization
4. Run `/optimize-images` for media
5. Set `published: true` or `draft: false`
6. Commit and push to trigger build

**Social Media Draft:**
Generate Twitter/LinkedIn announcement:
- Hook from introduction
- Key insight
- Link to post
- Relevant hashtags