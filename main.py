import text_extraction
import spelling_check
import time
import grammar_analyzer

file='ADITYA BANERJEE.pdf'
text=text_extraction.pdf_basics(file)
start_time=time.time()
#Printing the extracted text along with the page number:
for x,y in text.items():
    print(f"Page No: {x}")
    print(y)
    grammar_analyzer.grammar_analysis(y)

time_after_func1=time.time()
print(f'Time Now={(time_after_func1-start_time):.6f}')

#spelling_check.find_misspelled_words(text)


