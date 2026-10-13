# RAG and Document Loaders in LangChain

## What is RAG?

**RAG (Retrieval-Augmented Generation)** is a technique that combines information retrieval with language generation, where a model retrieves relevant informaation from a knowledge base and then uses them as context to generate accurate and grounded responses.

### Benefits
- Use of up-to-date information
- Better privacy
- No limit of document size

---

## Document Loaders

They are components in LangChain used to load data from various sources into a standardized format (usually as Document objects), which can then be used for chunking, embedding, retrieval and generation.

### Major Document Loaders
- `TextLoader`
- `PyPDFLoader`
- `WebBaseLoader`
- `CSVLoader`
- `DirectoryLoader`

---

## 1. TextLoader

It reads plain text files and converts them into LangChain Document objects.

**Use case:** Ideal for loading chat logs, scraped text, transcripts, code snippets or any plain text data into a LangChain pipeline.

---

## 2. PyPDFLoader

It is a document loader in LangChain used to load content from PDF files and convert each page into a Document object. It is used mostly when we have textual data in our PDFs.

**Limitation:** It uses the PyPDF library under the hood — not great with scanned PDFs or complex layouts.

### Alternatives

| Use Case | Recommended Loader |
|---|---|
| Simple, clean PDFs | `PyPDFLoader` |
| PDFs with tables/columns | `PDFPlumberLoader` |
| Scanned/image PDFs | `UnstructuredPDFLoader` or `AmazonTextractPDFLoader` |
| Need layout and image data | `PyMuPDFLoader` |
| Want best structure extraction | `UnstructuredPDFLoader` |

---

## 3. DirectoryLoader

It is a document loader that lets you load multiple documents from a directory (folder) of files.

### Glob Patterns

| Glob Pattern | What It Loads |
|---|---|
| `**/*.txt` | All `.txt` files in all subfolders |
| `*.pdf` | All `.pdf` files in the root folder |
| `data/*.csv` | All `.csv` files in the `data` directory |
| `**/*` | All files (any type, all folders) |

We can use `lazy_load()` for incremental loading of multiple documents.

---

## 4. WebBaseLoader

It is a document loader in LangChain used to load and extract text content from web pages (URLs). It uses BeautifulSoup under the hood to parse HTML and extract visible text.

**When to use:** For blogs, news articles or public websites where the content is primarily text-based and static.

---

## 5. CSVLoader

It is a document loader used to load CSV files into LangChain Document objects — one per row, by default.

---

## Custom Document Loaders

LangChain provides a wide range of built-in document loaders through `langchain-community` for sources such as Twitter, Reddit, WhatsApp, Dropbox, and AWS S3.

However, if we can't find a loader for our specific data source, we can also create our own **custom document loader** by creating a loader class and inheriting from the `BaseLoader` class.
