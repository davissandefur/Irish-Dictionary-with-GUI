# Breis.focloir.ie dictionary checker
# Saved as irish dictionary.py
# Created by Davis Sandefur; last update 11.12.14

import dictionary_classes

""" This file contains the main function, irish_dictionary, which combines all
the classes from the dictionary_classes.py folder to output the entries and
suggestions in list format, ready to be read off"""


def irish_dictionary(word, language, wordlist=[]):
    """ This function checks breis.focloir.ie for a word, Irish or English, and
    returns the word and related words. If no word exists, it returns similar
    words as given by the website.  """

    # Gets the entry and suggestions
    entry, suggestion = dictionary_classes.entry_lookup(word, language)
    
    # Get entries and suggestions in a list using HTMLRead class
    entries = dictionary_classes.entry_cleanup(entry)
    suggestions = dictionary_classes.entry_cleanup(suggestion)
    wordlist = dictionary_classes.word_store(word, wordlist)

    return entries, suggestions, wordlist

if __name__ == '__main__':
    irish_entry, irish_suggestions, irish_wordlist = irish_dictionary('gnóthach', 'irish')
    print(irish_wordlist) # Prints before English word gets added
    english_entry, english_suggestions, english_wordlist = irish_dictionary('hello', 'english')
    print(irish_entry)
    print()
    print(irish_suggestions)
    print()
    print(english_entry)
    print(english_suggestions)
    print()
    print(english_wordlist)