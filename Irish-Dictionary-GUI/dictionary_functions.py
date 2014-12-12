# Irish Dictionary Checker Modules
# Saved as dictionary_classes.py
# Created by Davis Sandefur; last updated 11.12.14

# TODO: Sound support for Irish words if sound available on breis.focloir.ie/fuaim

"""This module contains all the classes needed to scrub Breis.focloir.ie,
either in English or Irish , as well as the classes needed to parse the HTML
and create a running word list of the words.""" 


import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


def entry_lookup(word, language):
    """ This method searches and gets the data for entry and suggestion
    from breis.focloir.ie.
    """
    word = urllib.parse.quote_plus(word)
    language = language.lower()
    breis_slug = {"english": "eid", "irish": "fgb"}  # Path slug for breis
    response = urllib.request.urlopen("http://breis.focloir.ie/en/"+breis_slug[language]+'/'+word)
    html = response.read()
    soup = BeautifulSoup(html)
    entry = soup.findAll("div", class_=breis_slug[language] + " entry")
    suggestions = soup.findAll("div", class_="suggestions")
    return entry, suggestions
            

def entry_cleanup(html):
        """This function appends the text of the html to the list
        and returns it"""
        entries = []
        for b in html:
            entries.append(b.get_text())
        return entries


def word_store(word, wordlist):
    """ This function takes a word and a word list. If the word list is longer than 5 words, it deletes the last one
    and adds the word given to the front. If less than 5, it just adds it to the front.
    """
    wordlist.insert(0, word)
    if len(wordlist) > 5:
        wordlist.pop()
    return wordlist


def string_cleanup(string):
    """ This function takes a string with excess whitespace and cleans it upN
    """
    suggestions = str(string[0])
    suggestions = ' '.join(suggestions.split())

    return suggestions


def language_change(string):
    """ This function takes the cleaned up string of suggestions and changes "similar words" to the irish equivalent
    """
    words = string[16:]
    language_head = "Focail chosúla: "

    return language_head + words


if __name__ == "__main__":
    word_store_test = []  # Create a blank list to see if it'll add first
    for i in range(6):
        if i != 5:
            word_list = word_store("hello", word_store_test)  # Make first 5 words same to test if added
        elif i == 5:
            word_list = word_store("goodbye", word_store_test)  # Change word to see if it removed correctly
        print(word_store_test)

    # Gathering HTML about English word, reading the html to make it legibile as well as string cleanup on suggestions

    entry, suggestion = entry_lookup("hello", "English") # Returns HMTL markers
    clean_entry = entry_cleanup(entry)  # Should return list without HTML markers
    for i in clean_entry:
        print(i)

    print(entry_cleanup(suggestion))  # Should return string with whitespace markers
    print()
    clean_string = string_cleanup(entry_cleanup(suggestion))
    print(string_cleanup(clean_entry))  # Should return list of suggestions without needless whitespace
    print()
    print(clean_string)
    print()
    # Last test on language change. Changes "similar words" to "focail chósúla"
    print(language_change(clean_string))

    # Retest with Irish
    entry, suggestion = entry_lookup("gnóthach", "irish") # Returns HMTL markers
    clean_entry = entry_cleanup(entry)  # Should return list without HTML markers
    for i in clean_entry:
        print(i)

    print(entry_cleanup(suggestion))  # Should return string with whitespace markers
    print()
    clean_string = string_cleanup(entry_cleanup(suggestion))
    print(string_cleanup(clean_entry))  # Should return list of suggestions without needless whitespace
    print()
    print(clean_string)
    print()
    # Last test on language change. Changes "similar words" to "focail chósúla"
    print(language_change(clean_string))