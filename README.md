# Web2PDF

Web2PDF is a Python-based tool for converting web pages into PDF files. It includes scripts for both single-page and multiple-page conversions.

## Features

- Convert single web pages to PDF
- Batch convert multiple web pages to PDF
- Merge multiple PDF files into a single PDF (single-page conversion)
- Easy-to-use and customizable

## Installation

1. Clone the repository:

```bash
git clone https://github.com/anujbgit/web2pdf.git
cd web2pdf
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Single Page Conversion with Merging

Use `web2pdf-single.py` to convert a website and its linked pages into a single PDF file:

```bash
python web2pdf-single.py
```

You will be prompted to enter the URL of the website and the maximum number of pages to convert. If you leave the maximum pages blank, there will be no limit.

### Batch Conversion without Merging

Use `web2pdf.py` for batch conversion of a website and its linked pages into separate PDF files:

```bash
python web2pdf.py
```

You will be prompted to enter the URL of the website and the maximum number of pages to convert.

## Example

### Single Page Conversion

```bash
python web2pdf-single.py
Enter the URL of the website to convert: https://example.com
Enter the maximum number of pages to convert (leave blank for no limit): 10
```

This will convert up to 10 pages starting from `https://example.com` into a single PDF file named `website.pdf`.

### Batch Conversion

```bash
python web2pdf.py
Enter the URL of the website to convert: https://example.com
Enter the maximum number of pages to convert: 10
```

This will convert up to 10 pages starting from `https://example.com` into separate PDF files.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

---

For more details, visit the [Web2PDF GitHub page](https://github.com/anujbgit/web2pdf).
