What is RAG !!
--RAG is a technique that combines information retrieval with language generation, where a model retrieves relevant informaation from a knowledge base and then uses them as context to generate accurate and grounded responses.
Benefits:
--Use of up to date information
--Better Privacy
--No limit of document size
---
Document loaders:They are components in langchain used to load data from various sources into a standardized format(usually as document objects), which can then be used for chunking, embedding, retrieval and generation.
Major document loaders:
--TextLoader
--PyPDFLoader
--WebBaseLoader
--CSVLoader
--directoryLoader
---
TextLoader- It reads plain text files and converts them into langchain document object
Use case: Ideal for loading chat logs, scraped text, transcripts, code snippets or any plain text data into a langchain pipeline.
---
PyPDFLoader- It is a document loader in langchain used to load content from pdf files and convert each page into a document object. It is used mostly when we have textual data in our pdf.
Limitation- It uses the PyPDF library under the hood - not great with scanned pdfs or complex layouts.
Alternatives- 
    Use cases    -                  Recommended Loader
    Simple. clean pdfs              PyPDFLoader
    PDFs with tables/columns        PDFPlumberLoader
    Scanned/images Pdfs             UnstructuredPDFLoader or AmazonTextractPDFLoader
    Need layout and image data      PyMuPDFLoader
    Want best structure extarction  UnstructuredPDFLoader
---
DirectoryLoader- It is a document loader that lets you load multiple documents from a directory(folder) of files
Glob pattern    What it loads
"**/*.txt"      All .txt files in all subfolder
"*.pdf"         All .pdf files in root folder
"data/*.csv"    All .csv files in data directory
"**/*"          All files(any type, all folder)

We can use lazy_load for faster retrieval of multiple documents.
---
WebBaseLoader- It is a document loader in langchain used to load and extract text content from web pages(URLs). It uses BeautifulSoup under the hood to parse HTML and extarct visible text.
When to use: For blogs, news articles or public websites where the content is primarily text-based and static.
---
CSVLoader- It is document loader used to load csv files into langchain document objects - one per row, by default.
---
LangChain provides a wide range of built-in document loaders through `langchain-community` for sources such as Twitter, Reddit, WhatsApp, Dropbox, and AWS S3. However, if a loader for our specific data source is unavailable, we can create a **custom document loader** by defining a class that inherits from `BaseLoader` and implementing the required methods to load and convert data into LangChain `Document` objects.


