from langchain_text_splitters import MarkdownHeaderTextSplitter

markdown_text = """
# Student Tracker

This project manages student records.

## Features

- Add students
- View student details

## Tech Stack

- Python
- SQLite

### Installation

Install Python and clone the repository.
"""

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

documents = splitter.split_text(markdown_text)

for doc in documents:
    print("Metadata:", doc.metadata)
    print("Content:", doc.page_content)
    print("-" * 50)