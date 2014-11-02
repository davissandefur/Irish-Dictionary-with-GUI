# Irish Dictionary GUI
# Saved as dictionary_gui.py
# Last updated by: Davis Sandefur 2/11/14

# TODO: Add Irish Language Version

from tkinter import *
from irish_dictionary import irish_dictionary


class Callback:

    def english_callback():
        """Called when the user presses 'English'"""
        entries, suggestions, wordlist = irish_dictionary(frame1.entry.get(), 'English')
        for i in entries:
            frame3.st.insert(END, i)
            frame3.st.insert(END, '\n\n')
        suggestions = str(suggestions[0])
        suggestions = ' '.join(suggestions.split())
        frame3.st.insert(END, "\n")
        frame3.st.insert(END, suggestions)
        frame3.st.insert(END, "\n\nRecently used words: ")
        frame3.st.insert(END, wordlist)
        frame3.st.insert(END, "\n\n")

    def irish_callback():
        """Called when the user presses 'Irish'"""
        entries, suggestions, wordlist = irish_dictionary(frame1.entry.get(), 'Irish')
        for i in entries:
            frame3.st.insert(END, i)
            frame3.st.insert(END, "\n\n")
        suggestions = str(suggestions[0])
        suggestions = ' '.join(suggestions.split())
        frame3.st.insert(END, "\n")
        frame3.st.insert(END, suggestions)
        frame3.st.insert(END, "\n\nRecently used words: ")
        frame3.st.insert(END, wordlist)
        frame3.st.insert(END, "\n\n")


class FirstFrame():
    def __init__(self):
        self.frame1 = Frame()
        self.frame1.pack()
        l = Label(self.frame1, text="Enter your word:")
        l.pack(side=LEFT, expand=True, ipadx=100)
        self.entry = Entry(self.frame1)
        self.entry.pack(side=RIGHT, expand=True, ipadx=122)


class Buttons():
    def __init__(self):
        self.frame2 = Frame()
        self.frame2.pack()
        english_button = Button(self.frame2, text='English', command=Callback.english_callback)
        english_button.pack(side=LEFT, expand=True, ipadx=145)
        irish_button = Button(self.frame2, text='Irish', command=Callback.irish_callback)
        irish_button.pack(side=RIGHT, expand=True, ipadx=145)



class ScrollText():
    def __init__(self):
        self.frame3 = Frame()
        self.frame3.pack()
        self.st = Text(self.frame3)
        scrollbar = Scrollbar(self.frame3)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.st.yview)  # Linking scroll
        self.st.config(yscrollcommand=scrollbar.set)  # Linking scroll
        self.st.pack(side=LEFT, fill=BOTH, expand=1)


master = Tk()  # Create your Tk object
master.title("Irish Dictionary Searcher")
frame1 = FirstFrame()
frame2 = Buttons()
frame3 = ScrollText()


master.mainloop()
