# Irish Dictionary GUI
# Saved as dictionary_gui.py
# Last updated by: Davis Sandefur 29/10/14

""" This program brings together irish_dictionary.py and GUI.py, to make a
GUI that reports the entries for the word checked, suggestions, and a list,
with a scrollable text bar and option of choosing either Irish or English."""

from Gui import *
from irish_dictionary import *


g = Gui()
g.title("Irish Dictionary")


def english_callback():
    """Called when the user presses 'English'"""
    entries, suggestions, wordlist = irish_dictionary(entry.get(),'English')
    for i in entries:
        st.text.insert(END,i)
        st.text.insert(END,'\n\n')
    suggestions=str(suggestions[0])
    suggestions = ' '.join(suggestions.split())
    st.text.insert(END,"\n")
    st.text.insert(END,suggestions)
    st.text.insert(END,"\n\nRecently used words: ")
    st.text.insert(END,wordlist)
    st.text.insert(END,"\n\n")
    

    
        
def irish_callback():
    """Called when the user presses 'Irish'"""
    entries, suggestions, wordlist  = irish_dictionary(entry.get(),'Irish')
    for i in entries:
        st.text.insert(END,i)
        st.text.insert(END,"\n\n")
    suggestions=str(suggestions[0])
    suggestions = ' '.join(suggestions.split())
    st.text.insert(END,"\n")
    st.text.insert(END,suggestions)
    st.text.insert(END,"\n\nRecently used words: ")
    st.text.insert(END,wordlist)
    st.text.insert(END,"\n\n")
    



g.gr(cols=1)
entry = g.en()
g.endgr()
g.gr(cols=2)
engbutton= g.bu(text='English', command=english_callback)
irishbutton= g.bu(text='Irish', command=irish_callback)
g.endgr()

st = g.st()



