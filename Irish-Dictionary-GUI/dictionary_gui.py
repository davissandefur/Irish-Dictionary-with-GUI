# Irish Dictionary GUI
# Saved as dictionary_gui.py
# Last updated by: Davis Sandefur 31/10/14

from tkinter import *
from irish_dictionary import irish_dictionary

master = Tk()  # Create your Tk object

# Define callbacks


def english_callback():
    """Called when the user presses 'English'"""
    entries, suggestions, wordlist = irish_dictionary(entry.get(), 'English')
    for i in entries:
        st.insert(END, i)
        st.insert(END, '\n\n')
    suggestions = str(suggestions[0])
    suggestions = ' '.join(suggestions.split())
    st.insert(END, "\n")
    st.insert(END, suggestions)
    st.insert(END, "\n\nRecently used words: ")
    st.insert(END, wordlist)
    st.insert(END, "\n\n")


def irish_callback():
    """Called when the user presses 'Irish'"""
    entries, suggestions, wordlist = irish_dictionary(entry.get(), 'Irish')
    for i in entries:
        st.insert(END, i)
        st.insert(END, "\n\n")
    suggestions = str(suggestions[0])
    suggestions = ' '.join(suggestions.split())
    st.insert(END, "\n")
    st.insert(END, suggestions)
    st.insert(END, "\n\nRecently used words: ")
    st.insert(END, wordlist)
    st.insert(END, "\n\n")


# Create all widgets

# Create the first frame to hold the Label and entry widgets

frame1 = Frame(master)
frame1.pack()

l = Label(frame1, text="Enter your word:")
l.pack(side=LEFT, expand=True, ipadx=100)
entry = Entry(frame1)
entry.pack(side=RIGHT, expand=True, ipadx=122)

# Create a second frame to hold all your buttons

frame2 = Frame(master)
frame2.pack()

english_button = Button(frame2, text='English', command=english_callback)
english_button.pack(side=LEFT, expand=True, ipadx=145)
irish_button = Button(frame2, text='Irish', command=irish_callback)
irish_button.pack(side=RIGHT, expand=True, ipadx=145)


# Create the third frame to hold your scrollable text

frame3 = Frame(master)
frame3.pack()


st = Text(frame3)
scrollbar = Scrollbar(frame3)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=st.yview)  # Linking scroll
st.config(yscrollcommand=scrollbar.set)  # Linking scroll
st.pack(side=LEFT, fill=BOTH, expand=1)
master.mainloop()
