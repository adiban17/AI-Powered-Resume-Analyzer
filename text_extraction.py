import pdfplumber

# Extracting Text from the uploaded PDF File
def pdf_basics(file_path):

    extracted_text={}
    with pdfplumber.open(file_path) as pdf:
        total_pages=len(pdf.pages)
        #print(f'Number of Pages= {total_pages}')
        
        
        for x in range(0,total_pages):
            page=pdf.pages[x]
            extracted_text[x]=page.extract_text_simple(x_tolerance=3, y_tolerance=3)
    return extracted_text


#pdf_basics()
