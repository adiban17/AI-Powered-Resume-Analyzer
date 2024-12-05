from spellchecker import SpellChecker

spell = SpellChecker()

# Find misspelled words
def find_misspelled_words(file):

    

    for text in file.values():

    
        misspelled = spell.unknown(text.split())

        for word in misspelled:
            # Get the most likely correction
            
            if spell.correction(word)!=None:
                print(f"{word} -> {spell.correction(word)}")
