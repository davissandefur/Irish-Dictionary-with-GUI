# Breis.focloir.ie dictionary checker
# Saved as irish dictionary.py
# Created by Davis Sandefur; last update 29/10/14

import dictionary_classes

""" This file contains the main function, irish_dictionary, which combines all
the classes from the dictionary_classes.py folder to output the entries and
suggestions in list format, ready to be read off"""

def irish_dictionary(word,language,wordlist=[]):
    """ This function checks breis.focloir.ie for a word, Irish or English, and
    returns the word and related words. If no word exists, it returns similar
    words as given by the website.  """
    
    
        # Gets the entry and suggestions
    entry, suggestion = dictionary_classes.WordLookup(word,language).entry_lookup()
    
    # Get entires and suggestions in a list using HTMLRead class
    entries = dictionary_classes.HTMLRead(entry).append()
    suggestions = dictionary_classes.HTMLRead(suggestion).append()
    wordlist = dictionary_classes.WordStore(word,wordlist).append()

    return entries, suggestions, wordlist 

    
