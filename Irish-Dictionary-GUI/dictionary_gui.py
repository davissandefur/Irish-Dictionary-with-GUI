# Irish Dictionary GUI
# Saved as dictionary_gui.py
# Last updated by: Davis Sandefur 26/10/14

import TurtleWorld
from Gui import *
from irish_dictionary2 import *


g = Gui()
g.title("Irish Dictionary")
wordlist=[]

def callback1():
    """Called when the user presses 'English'"""
    entries, suggestions = irish_dictionary(entry.get(),'English')
    for i in entries:
        text.insert(END,i)
        text.insert(END,'\n\n')
    suggestions=str(suggestions[0])
    suggestions = ' '.join(suggestions.split())
    text.insert(END,"\n")
    text.insert(END,suggestions)
    wordlist.insert(0,entry.get())
    if len(wordlist)>5:
        wordlist.pop()
    text.insert(END,"\n\nRecently used words: ")
    text.insert(END,wordlist)
    text.insert(END,"\n")
    

    
        
def callback2():
    """Called when the user presses 'Irish'"""
    entries, suggestions  = irish_dictionary(entry.get(),'Irish')
    for i in entries:
        text.insert(END,i)
        text.insert(END,"\n\n")
    suggestions=str(suggestions[0])
    suggestions = ' '.join(suggestions.split())
    text.insert(END,"\n")
    text.insert(END,suggestions)
    wordlist.insert(0,entry.get())
    if len(wordlist)>5:
        wordlist.pop()
    text.insert(END,"\n\nRecently used words: ")
    text.insert(END,wordlist)
    text.insert(END,"\n")
    



g.gr(cols=1)
entry = g.en()
g.endgr()
g.gr(cols=2)
engbutton= g.bu(text='English', command=callback1)
irishbutton= g.bu(text='Irish', command=callback2)
g.endgr()

text = g.te(width=50, height=20)



