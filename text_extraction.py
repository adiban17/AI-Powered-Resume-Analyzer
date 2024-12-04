import pdfplumber

# Extracting Text from the uploaded PDF File
def pdf_basics():

    extracted_text={}
    with pdfplumber.open('ADITYA BANERJEE.pdf') as pdf:
        total_pages=len(pdf.pages)
        #print(f'Number of Pages= {total_pages}')
        
        
        for x in range(0,total_pages):
            page=pdf.pages[x]
            extracted_text[x]=page.extract_text_simple(x_tolerance=3, y_tolerance=3)
        
        # Printing the extracted text along with the page number:
        for x,y in extracted_text.items():
            print(f'Page No.{int(x)+1}')
            print(y)


pdf_basics()

from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))