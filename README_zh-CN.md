# PDF Craft Cloud

基于云服务的 PDF 转换工具包，可将 PDF 文档转换为 EPUB 和 Markdown 格式。

## 功能特性

- **PDF 转 EPUB**：将 PDF 文档转换为 EPUB 电子书格式
- **PDF 转 Markdown**：将 PDF 文档转换为 Markdown 格式
- **多种输入源**：支持本地文件和 URL 链接的 PDF
- **自动化处理**：自动完成上传、转换和下载流程

## 子流程

### File PDF to EPUB
将本地 PDF 文件转换为 EPUB 格式，自动完成上传和下载。

**输入：**
- `file`：本地 PDF 文件路径
- `saved_path`：EPUB 输出路径（可选）

**输出：**
- `saved_path`：下载的 EPUB 文件路径

### URL PDF to EPUB
通过云服务将 URL 链接的 PDF 转换为 EPUB 格式。

**输入：**
- `pdf_url`：PDF 文件的 URL 地址

**输出：**
- `download_url`：转换后 EPUB 文件的下载链接

### File PDF to Markdown
将本地 PDF 文件转换为 Markdown 格式，自动完成上传和下载。

**输入：**
- `file`：本地 PDF 文件路径
- `saved_path`：Markdown 输出路径（可选）

**输出：**
- `saved_path`：下载的 Markdown 文件路径

### URL PDF to Markdown
通过云服务将 URL 链接的 PDF 转换为 Markdown 格式。

**输入：**
- `pdf_url`：PDF 文件的 URL 地址

**输出：**
- `download_url`：转换后 Markdown 文件的下载链接

## 任务模块

| 任务 | 描述 |
|------|------|
| PDF to EPUB Submit | 提交 PDF URL 到转换服务并获取会话 ID |
| PDF to Markdown Submit | 提交 PDF URL 到 Markdown 转换服务并获取会话 ID |
| Poll PDF to EPUB Progress | 轮询转换进度，完成后返回下载链接 |
| Poll PDF to Markdown Progress | 轮询转换进度，完成后返回下载链接 |

## 使用方法

1. **本地 PDF 文件**：使用 "File PDF to EPUB" 或 "File PDF to Markdown" 子流程
2. **PDF URL 链接**：使用 "URL PDF to EPUB" 或 "URL PDF to Markdown" 子流程

转换过程完全自动化 - 文件会被上传到云存储，通过云服务转换，然后下载到您指定的位置。

## 依赖

- `upload-to-cloud`：云存储上传功能
- `downloader`：文件下载功能

## 安装

```bash
npm install
poetry install --no-root
```
