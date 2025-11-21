# PDF Craft Cloud

A cloud-based PDF conversion toolkit that transforms PDF documents into EPUB and Markdown formats using OOMOL's cloud services.

## Features

- **PDF to EPUB Conversion**: Convert PDF documents to EPUB e-book format
- **PDF to Markdown Conversion**: Convert PDF documents to Markdown format
- **Multiple Input Sources**: Support both local files and URL-based PDFs
- **Automatic File Handling**: Upload, convert, and download files automatically

## Subflows

### File PDF to EPUB
Convert a local PDF file to EPUB format with automatic upload and download.

**Inputs:**
- `file`: Local PDF file path
- `saved_path`: Output path for the EPUB file (optional)

**Outputs:**
- `saved_path`: Path of the downloaded EPUB file

### URL PDF to EPUB
Convert a PDF from URL to EPUB format via cloud service.

**Inputs:**
- `pdf_url`: URL of the PDF file to convert

**Outputs:**
- `download_url`: Download URL for the converted EPUB file

### File PDF to Markdown
Convert a local PDF file to Markdown format with automatic upload and download.

**Inputs:**
- `file`: Local PDF file path
- `saved_path`: Output path for the Markdown file (optional)

**Outputs:**
- `saved_path`: Path of the downloaded Markdown file

### URL PDF to Markdown
Convert a PDF from URL to Markdown format via cloud service.

**Inputs:**
- `pdf_url`: URL of the PDF file to convert

**Outputs:**
- `download_url`: Download URL for the converted Markdown file

## Task Blocks

| Task | Description |
|------|-------------|
| PDF to EPUB Submit | Submit a PDF URL to the conversion service and get a session ID |
| PDF to Markdown Submit | Submit a PDF URL to the Markdown conversion service and get a session ID |
| Poll PDF to EPUB Progress | Poll conversion progress and return download URL when complete |
| Poll PDF to Markdown Progress | Poll conversion progress and return download URL when complete |

## Usage

1. **For local PDF files**: Use "File PDF to EPUB" or "File PDF to Markdown" subflows
2. **For PDF URLs**: Use "URL PDF to EPUB" or "URL PDF to Markdown" subflows

The conversion process is fully automated - files are uploaded to cloud storage, converted via the cloud service, and downloaded to your specified location.

## Dependencies

- `upload-to-cloud`: Cloud storage upload functionality
- `downloader`: File download functionality

## Installation

```bash
npm install
poetry install --no-root
```
