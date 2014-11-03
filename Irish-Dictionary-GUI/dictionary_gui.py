# Irish Dictionary GUI
# Saved as dictionary_gui.py
# Last updated by: Davis Sandefur 2/11/14


from tkinter import *
from irish_dictionary import irish_dictionary
from dictionary_classes import StringCleanup


# TODO: Add Irish Language Version

class Callback:

    def english_callback():
        """Called when the user presses 'English'"""
        entries, suggestions, wordlist = irish_dictionary(frame1.entry.get(), 'English')
        for i in entries:
            frame3.st.insert(END, i)
            frame3.st.insert(END, '\n\n')
        suggestions = StringCleanup(suggestions).cleanup()
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
        suggestions = StringCleanup(suggestions).cleanup()
        frame3.st.insert(END, "\n")
        frame3.st.insert(END, suggestions)
        frame3.st.insert(END, "\n\nRecently used words: ")
        frame3.st.insert(END, wordlist)
        frame3.st.insert(END, "\n\n")


class FirstFrame(object):
    def __init__(self):
        self.frame1 = Frame()
        self.frame1.pack()
        self.entry = Entry(self.frame1)

        if language.language == 'English':
            l = Label(self.frame1, text="Enter your word:")
            l.pack(side=LEFT, expand=True, ipadx=50)
            language_button = Button(self.frame1, text="Leagan Gaeilge", command=language.english_to_irish)
            language_button.pack(side=RIGHT, padx=50)


        if language.language == 'Irish':
            l = Label(self.frame1, text="Cuir d'fhocal anseo")
            l.pack(side=LEFT, expand=True, ipadx=50)
            language_button = Button(self.frame1, text="English Version", command=language.irish_to_english)
            language_button.pack(side=RIGHT, padx=50)

        self.entry.pack(expand=True, ipadx=50)


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


class LanguageSwitcher:
    def __init__(self):
        self.language = 'English'  # English is default language


    def english_to_irish(self):
        """ This callback changes language to Irish  """
        self.language = 'Irish'
        print("This is being used")

    def irish_to_english(self):
        """ This callback changes language to English """
        self.language = 'English'
        print("This is being used")


master = Tk()  # Create your Tk object
master.title("Irish Dictionary Searcher")
language = LanguageSwitcher()
frame1 = FirstFrame()
frame2 = Buttons()
frame3 = ScrollText()


master.mainloop()
