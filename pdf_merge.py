from pypdf import PdfWriter,PdfReader
import os

def merge_pdfs_with_bookmarks(pdf_list, output_path):
    """合并PDF并添加书签"""
    merger = PdfWriter()
    current_page = 0
    for pdf_path in pdf_list:


        #添加PDF文件
        merger.append(pdf_path)
        # 添加书签（使用文件名作为书签名）
        bookmark_name = os.path.splitext(os.path.basename(pdf_path))[0]
        merger.add_outline_item(bookmark_name, current_page)#不pdf一个文件多页，这里不知道多少页，所以后面的代码读取文件页数进行校对位置

        # 1. 读取 PDF 文件
        reader = PdfReader(pdf_path)
        # 2. 获取总页数
        page_count = len(reader.pages)
        current_page += page_count
        reader.close()

    merger.write(output_path)
    merger.close()
    print(f"已创建带书签的PDF: {output_path}")

if __name__ == '__main__':
    pdf_file_list = ['1.pdf', '2.pdf', '3.pdf', '4.pdf', '5.pdf', '6.pdf', '7.pdf', '8.pdf', '9.pdf', '10.pdf', '11.pdf', '12.pdf', '13.pdf']
    merge_pdfs_with_bookmarks(pdf_file_list,'合并.pdf')