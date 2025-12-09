---
description: Analyze PRP against best practices and generate improvement prompt
argument-hint: [path-to-prp-file.md]
allowed-tools: Read, Grep, Glob, Bash
---

# PRP Analysis & Improvement Generator

This command analyzes your PRP against established best practices and generates actionable improvement prompts.

## Analyzing PRP: $1

### 🔍 PRP Analysis Results

**Reading PRP file...**

## 📊 PRP Quality Assessment

### ✅ **What's Working Well**
!Extract positive aspects from the PRP that follow best practices!

### ⚠️ **What's Missing or Unclear**
!Identify gaps, ambiguities, and incomplete sections!

### 🔧 **What Could Be Clearer**
!Find areas that need more specificity or better examples!

### ❌ **What Needs Improvement**
!Identify critical issues that violate PRP best practices!

## 🎯 Best Practices Analysis

### **"No Prior Knowledge" Test Check**
- [ ] **Goal Section**: Specific, measurable end state defined
- [ ] **Why Section**: Business value and user impact clear
- [ ] **What Section**: User-visible behavior with success criteria
- [ ] **Context Section**: All necessary references included
- [ ] **Implementation Blueprint**: Step-by-step tasks in dependency order
- [ ] **Validation Loop**: Executable testing strategy included

### **Information Density Check**
- [ ] **URLs**: Include specific sections/anchors, not just domains
- [ ] **File References**: Exact paths with line numbers and patterns to follow
- [ ] **Task Specifications**: Exact naming conventions and file placement
- [ ] **Validation Commands**: Project-specific and executable commands

### **Context Completeness Validation**
- [ ] **Documentation Links**: All necessary docs referenced with specific sections
- [ ] **Code Examples**: Relevant patterns from existing codebase included
- [ ] **Gotchas**: Library quirks and common pitfalls documented
- [ ] **Integration Points**: Clear API, database, and configuration touchpoints

### **Implementation Readiness**
- [ ] **Task Dependency Order**: Logical sequence from dependencies to implementation
- [ ] **Pattern References**: Existing codebase patterns to follow identified
- [ ] **Anti-Patterns**: What NOT to do explicitly stated
- [ ] **Success Criteria**: Measurable outcomes defined

## 🔧 Improvement Recommendations

### **Critical Issues (Must Fix)**
!List the most important issues that prevent single-pass implementation!

### **Important Improvements (Should Fix)**
!List significant enhancements that would improve implementation success!

### **Nice-to-Have Enhancements (Consider)**
!List minor improvements that would make the PRP even better!

## 📝 Improvement Prompt Generator

Based on the analysis, here's a prompt to improve your PRP:

### **Copy-Paste This Prompt to Update Your PRP:**

```markdown
Please update the PRP file at "$1" to address these specific improvements:

## Critical Improvements Needed:

!List the most critical issues with specific fixes needed!

## Important Enhancements Required:

!List significant improvements with specific actions!

## Context Additions Needed:

!List missing context, documentation, or examples that should be added!

## Validation Improvements:

!List validation steps that need to be added or clarified!

## Additional Research Required:

!If documentation or examples are missing, specify what needs to be researched!

**Please:**
1. Read the current PRP file at "$1"
2. Address all the improvement points listed above
3. Use Archon MCP server if additional documentation research is needed:
   - Use `rag_get_available_sources()` to find relevant documentation
   - Use `rag_search_knowledge_base()` for specific technical information
   - Use `rag_search_code_examples()` for implementation patterns
4. Maintain the existing PRP structure while enhancing completeness
5. Ensure all improvements follow the "No Prior Knowledge" test principle
6. Update the file directly with all improvements

**Focus on making every reference specific and actionable - no generic instructions or assumptions!**
```

## 🎯 Success Indicators

A high-quality PRP should score:
- **9-10**: Ready for single-pass implementation
- **7-8**: Minor improvements needed, good foundation
- **5-6**: Significant improvements required
- **<5**: Major restructuring needed

## 📈 Final Recommendation

!Provide overall assessment and recommendation for next steps!

---
*PRP Analysis completed for: $1*