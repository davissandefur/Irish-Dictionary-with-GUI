# Breis.focloir.ie dictionary checker
# Saved as irish dictionary.py
# Created by Davis Sandefur; last update 11.12.14

import dictionary_functions

""" This file contains the main function, irish_dictionary, which combines all
the classes from the dictionary_functions.py folder to output the entries and
suggestions in list format, ready to be read off"""


def irish_dictionary(word, language, version, wordlist=[]):
    """ This function checks breis.focloir.ie for a word, Irish or English, and
    returns the word and related words. If no word exists, it returns similar
    words as given by the website.  """

    # Gets the entry and suggestions
    entry, suggestion, form_of = dictionary_functions.entry_lookup(word, language, version)
    # Get entries and suggestions in a list using HTMLRead class
    entries = dictionary_functions.entry_cleanup(entry)
    suggestions = dictionary_functions.entry_cleanup(suggestion)
    suggestions = dictionary_functions.string_cleanup(suggestions)

    if form_of is not None:
        form_of = dictionary_functions.entry_cleanup(form_of)
        form_of = dictionary_functions.string_cleanup(form_of)
    wordlist = dictionary_functions.word_store(word, wordlist)

    return entries, suggestions, wordlist, form_of

if __name__ == '__main__':
    irish_entry, irish_suggestions, irish_wordlist, form_of = irish_dictionary('bí', 'irish', 'gaeilge')
    print(irish_wordlist)  # Prints before English word gets added
    english_entry, english_suggestions, english_wordlist, foo = irish_dictionary('hello', 'english', 'english')
    print(irish_entry)
    print()
    print(irish_suggestions)
    print()
    print(english_entry)
    print(english_suggestions)
    print()
    print(english_wordlist)