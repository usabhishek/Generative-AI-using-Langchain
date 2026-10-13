# Text Splitting in LangChain

## What is Text Splitting?

Text splitting is the process of breaking large pieces of text (such as articles, PDFs, HTML pages, or books) into smaller, manageable pieces called **chunks** that an LLM can process efficiently.

## Why Do We Need Chunking?

### 1. Overcoming Model Limitations
Many embedding models and language models have maximum input size constraints (context windows). Splitting allows us to process documents that would otherwise exceed these limits.

### 2. Improving Downstream Tasks

Text splitting improves the performance of LLM-powered tasks:

- **Embeddings:** Smaller, focused chunks can produce more relevant vector representations.
- **Semantic Search:** Search results point to specific, relevant information rather than unrelated content.
- **Summarization:** Smaller chunks help maintain focus and reduce topic drift.

### 3. Optimizing Computational Resources

Working with smaller chunks of text can be more memory-efficient and allow for better parallelization of processing tasks.

---

## Major Types of Text Splitters

### 1. Length-Based Splitters

Split text according to a specified character or token length.

**Examples:**
- `CharacterTextSplitter`
- `RecursiveCharacterTextSplitter`

### 2. Token-Based Splitters

Split text according to token count rather than character count.

**Example:**
- `TokenTextSplitter`

### 3. Text-Structure-Based Splitters

Split text using structural elements such as paragraphs, sentences, or separators.

**Examples:**
- `RecursiveCharacterTextSplitter`
- `CharacterTextSplitter`

### 4. Document-Structure-Based Splitters

Split documents according to their structure, preserving meaningful sections and hierarchy.

**Examples:**
- `MarkdownHeaderTextSplitter` — Separates Markdown content based on headings.
- `HTMLHeaderTextSplitter` — Splits HTML content based on heading tags.
- `PythonCodeTextSplitter` — Splits Python code using language-aware separators.

---

## RecursiveCharacterTextSplitter vs. MarkdownHeaderTextSplitter

Both can be used to split Markdown documents, but they serve different purposes.

| Feature | `RecursiveCharacterTextSplitter.from_language(Language.MARKDOWN)` | `MarkdownHeaderTextSplitter` |
|---|---|---|
| **Main purpose** | Splits text by size using Markdown-aware separators | Splits text based on heading hierarchy |
| **`chunk_size`** | Supported | Not supported directly |
| **`chunk_overlap`** | Supported | Not supported directly |
| **Heading metadata** | Not automatically added as heading metadata | Stores heading information in metadata |
| **Preserves structure** | Tries to preserve logical text boundaries | Uses headings to define sections |
| **Best use** | Controlling chunk size | Preserving document structure |

### Using Both Together

For a RAG pipeline, both splitters can be combined:

1. Use `MarkdownHeaderTextSplitter` to divide the document into logical sections based on headings.
2. Use `RecursiveCharacterTextSplitter` to split oversized sections into smaller chunks of a specified size.

This approach helps preserve document structure while maintaining manageable chunk sizes.

---

## Key Takeaway

Effective text splitting helps preserve context, improve retrieval relevance, and prepare documents for embedding generation and retrieval in RAG pipelines.