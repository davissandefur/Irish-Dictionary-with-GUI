# Irish Dictionary GUI
# Saved as dictionary_gui.py
# Last updated by: Davis Sandefur 7/11/14

from tkinter import *
from irish_dictionary import irish_dictionary
from dictionary_classes import StringCleanup


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

    def english_to_irish():
        """ This is called when the button to turn the interface to Irish is pressed"""
        frame1.entry.pack_forget()  # Forget English entry
        frame1.entry = Entry(frame1.irish_frame, text="Cuir d'fhocal anseo")  # Create new entry for Irish version
        frame1.entry.pack(expand=True, fill=Y)
        frame1.english_frame.pack_forget()  # Forget English version of input
        frame1.irish_frame.pack(expand=True, fill=Y)
        frame2.english_frame.pack_forget()  # Forget the English buttons
        frame2.irish_frame.pack(expand=True, fill=Y)
        frame3.frame3.pack_forget()  # Remove scrollable text from top
        frame3.frame3.pack(expand=True, fill=BOTH)  # Repack scrollable text at bottom

    def irish_to_english():
        """ This is called when th button to turn the interface to English is pressed """
        frame1.entry.pack_forget()  # Forget the Irish entry
        frame1.entry = Entry(frame1.english_frame, text="Enter your word here")  # Create new entry with English version
        frame1.entry.pack(expand=True, fill=BOTH)
        frame1.irish_frame.pack_forget()  # Forget the rest of the Irish input version
        frame1.english_frame.pack(expand=True, fill=Y)
        frame2.irish_frame.pack_forget()  # Forget the Irish buttons
        frame2.english_frame.pack(expand=True, fill=Y)
        frame3.frame3.pack_forget()  # Remove scrollable text from top
        frame3.frame3.pack(expand=True, fill=BOTH)  # Repack scrollable text at bottom


class FirstFrame(object):
    def __init__(self, root):
        # Create a frame for the English version
        self.english_frame = Frame(root)
        self.english_frame.pack(expand=True, fill=Y)  # English is default version
        self.entry = Entry(self.english_frame)
        english_label = Label(self.english_frame, text="Enter your word:")
        english_label.pack(side=LEFT, expand=True, ipadx=50, fill=Y)
        english_language_button = Button(self.english_frame, text="Leagan Gaeilge", command=Callback.english_to_irish)
        english_language_button.pack(side=RIGHT, padx=50, fill=Y)

        # Create a frame for the Irish version
        self.irish_frame = Frame(root)
        irish_label = Label(self.irish_frame, text="Cuir d'fhocal anseo")
        irish_label.pack(side=LEFT, expand=True, ipadx=50, fill=Y)
        irish_language_button = Button(self.irish_frame, text="English Version", command=Callback.irish_to_english)
        irish_language_button.pack(side=RIGHT, padx=50, fill=Y)
        self.entry.pack(expand=True, ipadx=50, fill=Y)  # Pack entry at the very end


class Buttons(object):
    def __init__(self, root):

        # Create a frame for the English language buttons
        self.english_frame = Frame(root)
        self.english_frame.pack(expand=True, fill=Y)
        english_button = Button(self.english_frame, text='English', command=Callback.english_callback)
        english_button.pack(side=LEFT, expand=True, ipadx=145, fill=Y)
        irish_button = Button(self.english_frame, text='Irish', command=Callback.irish_callback)
        irish_button.pack(side=RIGHT, expand=True, ipadx=145, fill=Y)

        # Create a second frame to hold the Irish language buttons
        self.irish_frame = Frame(root)
        bearla_button = Button(self.irish_frame, text='Béarla', command=Callback.english_callback)
        bearla_button.pack(side=LEFT, expand=True, ipadx=145, fill=Y)
        gaeilge_button = Button(self.irish_frame, text='Gaeilge', command=Callback.irish_callback)
        gaeilge_button.pack(side=RIGHT, expand=True, ipadx=145, fill=Y)


class ScrollText(object):
    def __init__(self, root):
        self.frame3 = Frame(root)
        self.frame3.pack(expand=True, fill=BOTH)
        self.st = Text(self.frame3)
        scrollbar = Scrollbar(self.frame3)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.st.yview)  # Linking scroll
        self.st.config(yscrollcommand=scrollbar.set)  # Linking scroll
        self.st.pack(side=LEFT, fill=BOTH, expand=1)

master = Tk()  # Create your Tk object
master.title("Irish Dictionary Searcher")
frame1 = FirstFrame(master)
frame2 = Buttons(master)
frame3 = ScrollText(master)
master.mainloop()
