# PDF Concatenator (PDF 合并器)

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

一个简单实用的 Python 工具，用于自动合并指定目录下的所有 PDF 文件，并提取其中的金额信息。

## 功能特点

- 📄 自动扫描 `pdfs/` 目录下的所有 PDF 文件
- 🔗 按文件名排序后合并为一个 PDF 文件
- 💰 自动提取合并后文档中的金额信息（¥ 符号开头的数字）
- 🚀 基于 PyPDF2 库，轻量快速

## 环境要求

- Python 3.10 或更高版本
- [uv](https://github.com/astral-sh/uv)（快速 Python 包管理器）

## 安装与使用

### 1. 克隆或下载项目

```bash
git clone "https://github.com/bryantaolong/pdf_concatenator.git"
cd pdf_concatenator
```

### 2. 目录结构

目录结构示例：
```
pdf_concatenator/
├── main.py
├── README.md
└── pdfs/
    ├── 文档1.pdf
    ├── 文档2.pdf
    └── 文档3.pdf
```

### 3. 安装依赖

使用 `uv` 安装依赖（推荐）：

```bash
uv add PyPDF2
```

或者使用传统的 `pip`：

```bash
pip install PyPDF2
```

### 4. 运行程序

```bash
uv run main.py
```

或者：

```bash
python main.py
```

## 使用说明

1. 将要合并的 PDF 文件放入 `pdfs/` 目录
2. 运行程序
3. 程序会自动：
   - 扫描目录中的所有 PDF 文件
   - 按文件名排序后合并
   - 生成 `合并结果.pdf` 文件
   - 提取并显示文档中的金额信息

## 输出示例

```
找到 2 个 PDF 文件：
  - 539-龙涛.pdf
  - Git Cheat Sheet.pdf
已添加：539-龙涛.pdf
已添加：Git Cheat Sheet.pdf

PDF合并完成！已保存为：合并结果.pdf

提取到的金额信息：['¥1,000.00', '¥2,500.00']
```

## 自定义配置

### 修改合并后的文件名

在 `main.py` 中找到以下代码行：

```python
output_filename = "合并结果.pdf"
```

修改为你想要的文件名即可。

### 修改金额提取规则

当前正则表达式为 `r'¥[\d,]+\.?\d*'`，匹配以 ¥ 开头、包含数字和逗号的金额。如需修改，调整第 52 行的正则表达式：

```python
amounts = re.findall(r'¥[\d,]+\.?\d*', text)
```

例如，匹配美元金额：
```python
amounts = re.findall(r'\$[\d,]+\.?\d*', text)
```

## 常见问题

### Q: 为什么提示"没有找到任何 PDF 文件"？
A: 请确保：
- `pdfs/` 目录存在于项目根目录
- 目录中包含 `.pdf` 后缀的文件
- 文件名没有特殊字符导致读取失败

### Q: 合并后的 PDF 顺序不对？
A: 程序默认按文件名排序。如需自定义顺序，可以在文件名前添加数字前缀，如：
- `01_文档1.pdf`
- `02_文档2.pdf`

### Q: 提取中文 PDF 文本时出现乱码？
A: PyPDF2 对某些中文字体支持有限。如遇此问题，可考虑更换为 `pdfplumber` 或 `pypdf`：

```bash
uv add pdfplumber
```

然后修改代码中的 PDF 读取部分。

## 技术栈

- Python 3.13+
- PyPDF2 - PDF 处理库
- pathlib - 文件路径处理
- re - 正则表达式匹配

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
