import PyPDF2
import re
import os, sys
import time
 
def split_pdf(filename, text_to_split):
    try:
        pdf_file = open(filename, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
       
        page_count = 1
        start_page = 0
        for page_num in range(num_pages):
          page = pdf_reader.pages[page_num]
          text = page.extract_text().strip()
          if "STATEMENT" in text and "Date:" in text:
              result = re.search('STATEMENT(\n.*\n)Date:', text)
              customerNumber = result.group(1).strip()
          if text_to_split in text:
            new_filename = new_Split_PDFs_path+"\\"+customerNumber+".pdf"
            with open(new_filename, 'wb') as new_pdf_file:
              pdf_writer = PyPDF2.PdfWriter()
              for i in range(start_page, page_num + 1):
                pdf_writer.add_page(pdf_reader.pages[i])
              pdf_writer.write(new_pdf_file)
            start_page = page_num + 1
            page_count += 1
            
        pdf_file.close()
        return 'Successful'
    except Exception as e:
        return 'Failed to execute: '+e
 


filename = str(sys.argv[1])
new_Split_PDFs_path = filename[:filename.rfind("\\")]+"\SplitPDFs"
#Creating Split PDFs folder f not exists
if not os.path.exists(new_Split_PDFs_path):
    os.makedirs(new_Split_PDFs_path)
text_to_split = "Total"
return_Output = split_pdf(filename, text_to_split)
print(return_Output)