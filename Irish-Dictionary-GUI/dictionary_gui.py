# Irish Dictionary GUI
# Saved as dictionary_gui.py
# Last updated by: Davis Sandefur 15/11/14

# TODO: Sound support for Irish words if sound available on breis.focloir.ie/fuaim

from tkinter import *
from irish_dictionary import irish_dictionary
from dictionary_classes import StringCleanup, SuggestionsToIrish


class Callback:
    """ This class contains all callbacks for the program
    """

    @staticmethod
    def bearla_callback():
        """ Called when user presses 'Béarla'
        """
        entries, suggestions, wordlist = irish_dictionary(irish_label.entry.get(), 'English')
        for i in entries:
            text_widget.st.insert(END, i)
            text_widget.st.insert(END, '\n\n')
        suggestions = StringCleanup(suggestions).cleanup()
        suggestions = SuggestionsToIrish(suggestions).language_change()
        text_widget.st.insert(END, "\n")
        text_widget.st.insert(END, suggestions)
        text_widget.st.insert(END, "\n\nNa focail is déanaí: ")
        text_widget.st.insert(END, wordlist)
        text_widget.st.insert(END, "\n\n")
        text_widget.st.see(END)

    @staticmethod
    def gaeilge_callback():
        """ Called when user presses 'Gaeilge'
        """
        entries, suggestions, wordlist = irish_dictionary(irish_label.entry.get(), 'Irish')
        for i in entries:
            text_widget.st.insert(END, i)
            text_widget.st.insert(END, '\n\n')
        suggestions = StringCleanup(suggestions).cleanup()
        suggestions = SuggestionsToIrish(suggestions).language_change()
        text_widget.st.insert(END, "\n")
        text_widget.st.insert(END, suggestions)
        text_widget.st.insert(END, "\n\nNa focail is déanaí: ")
        text_widget.st.insert(END, wordlist)
        text_widget.st.insert(END, "\n\n")
        text_widget.st.see(END)

    @staticmethod
    def english_callback():
        """Called when the user presses 'English'"""
        entries, suggestions, wordlist = irish_dictionary(english_label.entry.get(), 'English')
        for i in entries:
            text_widget.st.insert(END, i)
            text_widget.st.insert(END, '\n\n')
        suggestions = StringCleanup(suggestions).cleanup()
        text_widget.st.insert(END, "\n")
        text_widget.st.insert(END, suggestions)
        text_widget.st.insert(END, "\n\nRecently used words: ")
        text_widget.st.insert(END, wordlist)
        text_widget.st.insert(END, "\n\n")
        text_widget.st.see(END)

    @staticmethod
    def irish_callback():
        """Called when the user presses 'Irish'"""
        entries, suggestions, wordlist = irish_dictionary(english_label.entry.get(), 'Irish')
        for i in entries:
            text_widget.st.insert(END, i)
            text_widget.st.insert(END, "\n\n")
        suggestions = StringCleanup(suggestions).cleanup()
        text_widget.st.insert(END, "\n")
        text_widget.st.insert(END, suggestions)
        text_widget.st.insert(END, "\n\nRecently used words: ")
        text_widget.st.insert(END, wordlist)
        text_widget.st.insert(END, "\n\n")
        text_widget.st.see(END)

    @staticmethod
    def english_to_irish():
        """ This is called when the button to turn the interface to Irish is pressed"""
        english_label.english_frame.pack_forget()
        irish_label.irish_frame.pack(expand=True, fill=Y)
        english_buttons.english_frame.pack_forget()  # Forget the English buttons
        irish_buttons.irish_frame.pack(expand=True, fill=Y)
        text_widget.text_widget.pack_forget()  # Remove scrollable text from top
        text_widget.text_widget.pack(expand=True, fill=BOTH)  # Repack scrollable text at bottom
        text_widget.st.see(END)

    @staticmethod
    def irish_to_english():
        """This is called when th button to turn the interface to English is pressed"""
        irish_label.irish_frame.pack_forget()
        english_label.english_frame.pack()
        irish_buttons.irish_frame.pack_forget()  # Forget the Irish buttons
        english_buttons.english_frame.pack(expand=True, fill=Y)
        text_widget.text_widget.pack_forget()  # Remove scrollable text from top
        text_widget.text_widget.pack(expand=True, fill=BOTH)  # Repack scrollable text at bottom
        text_widget.st.see(END)


class EnglishLabel(object):
    """ This class contains the English version of the labels for the word input
    """
    def __init__(self, root):
        # Create a frame for the English version
        self.english_frame = Frame(root)
        self.english_frame.pack(expand=True, fill=Y)  #
        self.entry = Entry(self.english_frame)
        english_label = Label(self.english_frame, text="Enter your word:")
        english_label.pack(side=LEFT, expand=True, ipadx=50, fill=Y)
        english_language_button = Button(self.english_frame, text="Leagan Gaeilge", command=Callback.english_to_irish)
        english_language_button.pack(side=RIGHT, padx=50, fill=Y)
        self.entry.pack(expand=True, ipadx=50, fill=Y)  # Pack entry at the very end


class IrishLabel(object):
    """ This class contains the Irish version of the labels for the word input
    """
    def __init__(self, root):
        self.irish_frame = Frame(root)
        # Create a frame for the Irish version
        self.entry = Entry(self.irish_frame)
        irish_label = Label(self.irish_frame, text="Cuir d'fhocal anseo")
        irish_label.pack(side=LEFT, expand=True, ipadx=50, fill=Y)
        irish_language_button = Button(self.irish_frame, text="English Version", command=Callback.irish_to_english)
        irish_language_button.pack(side=RIGHT, padx=50, fill=Y)
        self.entry.pack(expand=True, ipadx=50, fill=Y)  # Pack entry at the very end


class EnglishButtons(object):
    """ This class contains the English version of buttons that determine which language is searched
    """
    def __init__(self, root):
        # Create a frame for the English language buttons
        self.english_frame = Frame(root)
        self.english_frame.pack(expand=True, fill=Y)
        english_button = Button(self.english_frame, text='English', command=Callback.english_callback)
        english_button.pack(side=LEFT, expand=True, ipadx=145, fill=Y)
        irish_button = Button(self.english_frame, text='Irish', command=Callback.irish_callback)
        irish_button.pack(side=RIGHT, expand=True, ipadx=145, fill=Y)


class IrishButtons(object):
    """ This class contains the Irish version of buttons that determine which language is searched
    """
    def __init__(self, root):
        # Create a second frame to hold the Irish language buttons
        self.irish_frame = Frame(root)
        bearla_button = Button(self.irish_frame, text='Béarla', command=Callback.bearla_callback)
        bearla_button.pack(side=LEFT, expand=True, ipadx=145, fill=Y)
        gaeilge_button = Button(self.irish_frame, text='Gaeilge', command=Callback.gaeilge_callback)
        gaeilge_button.pack(side=RIGHT, expand=True, ipadx=145, fill=Y)


class ScrollText(object):
    """ This class contains a scrollable text widget
    """
    def __init__(self, root):
        self.text_widget = Frame(root)
        self.text_widget.pack(expand=True, fill=BOTH)
        self.st = Text(self.text_widget)
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.st.yview)  # Linking scroll
        self.st.config(yscrollcommand=scrollbar.set)  # Linking scroll
        self.st.pack(side=LEFT, fill=BOTH, expand=1)

master = Tk()  # Create your Tk object
master.title("Irish Dictionary Searcher")
english_label = EnglishLabel(master)
irish_label = IrishLabel(master)
english_buttons = EnglishButtons(master)
irish_buttons = IrishButtons(master)
text_widget = ScrollText(master)
master.mainloop()
