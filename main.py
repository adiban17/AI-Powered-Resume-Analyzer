import text_extraction
import spelling_check

file='ADITYA BANERJEE.pdf'
text=text_extraction.pdf_basics(file)

# Printing the extracted text along with the page number:
'''
for x,y in text.items():
    print(f"Page No: {x}")
    print(y)
'''


spelling_check.find_misspelled_words(text)
