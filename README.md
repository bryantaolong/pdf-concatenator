# PDF Concatenator

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A simple and practical Python tool that automatically merges all PDF files in a specified directory and extracts amount information from them.

## Features

- 📄 Automatically scans all PDF files in the `pdfs/` directory
- 🔗 Merges them into a single PDF file after sorting by filename
- 💰 Automatically extracts amount information (numbers starting with ¥) from the merged document
- 🚀 Lightweight and fast, based on the pypdf library

## Requirements

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) (fast Python package manager)

## Installation & Usage

### 1. Clone or download the project

```bash
git clone "https://github.com/bryantaolong/pdf_concatenator.git"
cd pdf_concatenator
```

### 2. Directory Structure

Example directory structure:
```
pdf_concatenator/
├── main.py
├── README.md
└── pdfs/
    ├── document1.pdf
    ├── document2.pdf
    └── document3.pdf
```

### 3. Install Dependencies

Install dependencies using `uv` (recommended):

```bash
uv add pypdf
```

Or use traditional `pip`:

```bash
pip install pypdf
```

### 4. Run the program

```bash
uv run main.py
```

Or:

```bash
python main.py
```

## Usage Instructions

1. Put the PDF files you want to merge into the `pdfs/` directory
2. Run the program
3. The program will automatically:
   - Scan all PDF files in the directory
   - Merge them after sorting by filename
   - Generate a `r.pdf` file
   - Extract and display amount information from the documents

## Output Example

```
Found 2 PDF files:
  - 539.pdf
  - Git Cheat Sheet.pdf
Added: 539.pdf
Added: Git Cheat Sheet.pdf

PDF merge complete! Saved as: r.pdf

Extracted amount information: ['¥1,000.00', '¥2,500.00']
```

## Customization

### Change the output filename

Find the following line in `main.py`:

```python
output_filename = "r.pdf"
```

Change it to the filename you want.

### Modify the amount extraction rules

The current regular expression is `r'¥[\d,]+\.?\d*'`, which matches amounts starting with ¥, containing digits and commas. To modify it, adjust the regular expression on line 52:

```python
amounts = re.findall(r'¥[\d,]+\.?\d*', text)
```

For example, to match USD amounts:
```python
amounts = re.findall(r'\$[\d,]+\.?\d*', text)
```

## FAQ

### Q: Why does it say "No PDF files found"?

A: Please ensure:
- The `pdfs/` directory exists in the project root
- The directory contains files with the `.pdf` extension
- The filenames don't contain special characters that cause read failures

### Q: The order of the merged PDF is wrong?

A: The program sorts by filename by default. To customize the order, you can add numeric prefixes to the filenames, such as:
- `01_document1.pdf`
- `02_document2.pdf`

### Q: Garbled text when extracting Chinese PDF text?

A: PyPDF2 has limited support for some Chinese fonts. If you encounter this issue, consider switching to `pdfplumber` or `pypdf`:

```bash
uv add pdfplumber
```

Then modify the PDF reading part in the code.

## Tech Stack

- Python 3.13+
- pypdf - PDF processing library
- pathlib - File path handling
- re - Regular expression matching

## License

MIT License

## Contributing

Issues and Pull Requests are welcome!
