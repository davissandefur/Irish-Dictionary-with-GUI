<<<<<<< HEAD:Irish-Dictionary-GUI/dictionary_classes.py
# Irish Dictionary Checker Modules
# Saved as dictionary_classes.py
# Created by Davis Sandefur; last updated 29.10.14

"""This module contains all the classes needed to scrub Breis.focloir.ie,
either in English or Irish , as well as the classes needed to parse the HTML
and create a running word list of the words.""" 

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

class WordLookup(object): # Create a class to look up the word
    """ This class searches breis.focloir.ie for a word and returns the
    div ready to be parsed. """
    def __init__(self,word,language):
        self.word = urllib.parse.quote_plus(word)
        self.language = language
        
=======
# Irish Dictionary GUI
# Saved as dictionary_gui.py
# Last updated by: Davis Sandefur 26/10/14

from Gui import *
from irish_dictionary2 import *


g = Gui()
g.title("Irish Dictionary")
wordlist=[]

def callback1():
    """Called when the user presses 'English'"""
    entries, suggestions = irish_dictionary(entry.get(),'English')
    for i in entries:
        st.text.insert(END,i)
        st.text.insert(END,'\n\n')
    suggestions=str(suggestions[0])
    suggestions = ' '.join(suggestions.split())
    st.text.insert(END,"\n")
    st.text.insert(END,suggestions)
    wordlist.insert(0,entry.get())
    if len(wordlist)>5:
        wordlist.pop()
    st.text.insert(END,"\n\nRecently used words: ")
    st.text.insert(END,wordlist)
    st.text.insert(END,"\n\n")
>>>>>>> origin/master:Irish-Dictionary-GUI/irish_dictionary2.py
    

<<<<<<< HEAD:Irish-Dictionary-GUI/dictionary_classes.py
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
=======
    
        
def callback2():
    """Called when the user presses 'Irish'"""
    entries, suggestions  = irish_dictionary(entry.get(),'Irish')
    for i in entries:
        st.text.insert(END,i)
        st.text.insert(END,"\n\n")
    suggestions=str(suggestions[0])
    suggestions = ' '.join(suggestions.split())
    st.text.insert(END,"\n")
    st.text.insert(END,suggestions)
    wordlist.insert(0,entry.get())
    if len(wordlist)>5:
        wordlist.pop()
    st.text.insert(END,"\n\nRecently used words: ")
    st.text.insert(END,wordlist)
    st.text.insert(END,"\n\n")
    



g.gr(cols=1)
entry = g.en()
g.endgr()
g.gr(cols=2)
engbutton= g.bu(text='English', command=callback1)
irishbutton= g.bu(text='Irish', command=callback2)
g.endgr()

st = g.st()
>>>>>>> origin/master:Irish-Dictionary-GUI/irish_dictionary2.py
