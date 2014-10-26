# Breis.focloir.ie dictionary checker
# Saved as irish dictionary.py
# Created by Davis Sandefur; last update 25/10/14


import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

class WordLookup(object): # Create a class to look up the word
    """ This class searches breis.focloir.ie for a word and returns the
    div ready to be parsed. """
    def __init__(self,word,language):
        self.word = urllib.parse.quote_plus(word)
        self.language = language
    
    def entry_lookup(self):
        """ This method searches and gets the data for entry and suggestion
        from breis.focloir.ie.
        """
        breis_slug = {"English": "eid", "Irish": "fgb"} # Path slug for breis
        response = urllib.request.urlopen("http://breis.focloir.ie/en/"+breis_slug[self.language]+"/"+self.word)
        html = response.read()
        soup = BeautifulSoup(html)
        entry = soup.findAll("div", class_=breis_slug[self.language] + " entry") 
        suggestions = soup.findAll("div", class_="suggestions")
        return entry, suggestions
            

class HTMLRead(object):
    """ This class reads the HTML and gets the text in a list ready to be
    read by the program. """
    def __init__(self,html):
        self.html = html
    entries = [] # Create a blank list to append to
    def append(self):
        """This function appends the text of the html to the list
        and returns it"""
        entries = []
        for b in self.html:
            entries.append(b.get_text())
        return entries

class WordStore(object):
    """ This class is used to store a word."""
    def __init__(self,word,wordlist):
        self.word = word
        self.wordlist = wordlist

    
    def append(self):
        self.wordlist.insert(0,self.word)
        if len(self.wordlist)> 5:
            self.wordlist.pop()
        return self.wordlist
    
def irish_dictionary(word,language,wordlist=[]):
    """ This function checks breis.focloir.ie for a word, Irish or English, and
    returns the word and related words. If no word exists, it returns similar
    words as given by the website.  """
    
    # Gets the entry and suggestions
    entry, suggestion = WordLookup(word,language).entry_lookup()
    
    # Get entires and suggestions in a list using HTMLRead class
    entries = HTMLRead(entry).append()
    suggestions = HTMLRead(suggestion).append()
    #wordlist = WordStore(word,wordlist).append()

    return entries, suggestions 

    
    
       
if __name__ == '__main__':
    irish_dictionary()
