from pypdf import PdfWriter, PdfReader
import re
import os
from pathlib import Path


def get_pdfs_from_directory() -> list:
    """从根目录下的 pdfs/ 目录中读取所有 PDF 文件"""
    # 获取当前脚本所在的根目录（或当前工作目录）
    current_dir = Path.cwd()  # 或者用 Path(__file__).parent 获取脚本所在目录
    pdf_dir = current_dir / "pdfs"

    # 检查目录是否存在
    if not pdf_dir.exists():
        print(f"错误：目录 '{pdf_dir}' 不存在！")
        return []
    
    # 获取所有 .pdf 文件（不区分大小写）
    pdf_files = list(pdf_dir.glob("*.pdf"))
    
    # 转换为字符串路径并排序（可选，让合并顺序更可控）
    pdf_files = [str(pdf) for pdf in sorted(pdf_files)]
    
    if not pdf_files:
        print(f"警告：目录 '{pdf_dir}' 中没有找到 PDF 文件！")
    else:
        print(f"找到 {len(pdf_files)} 个 PDF 文件：")
        for pdf in pdf_files:
            print(f"  - {os.path.basename(pdf)}")
    
    return pdf_files


def main() -> None:
    # 从 pdfs/ 目录读取所有 PDF 文件
    pdf_files = get_pdfs_from_directory()
    
    if not pdf_files:
        print("没有找到任何 PDF 文件，程序退出。")
        return
    
    # 合并PDF (pypdf 6.x 使用 PdfWriter + PdfReader)
    writer = PdfWriter()
    
    for pdf in pdf_files:
        try:
            reader = PdfReader(pdf)
            for page in reader.pages:
                writer.add_page(page)
            print(f"已添加：{os.path.basename(pdf)}")
        except Exception as e:
            print(f"添加文件 '{pdf}' 时出错：{e}")
    
    output_filename = "合并结果.pdf"
    with open(output_filename, "wb") as output_file:
        writer.write(output_file)
    print(f"\nPDF合并完成！已保存为：{output_filename}")


if __name__ == "__main__":
    main()
