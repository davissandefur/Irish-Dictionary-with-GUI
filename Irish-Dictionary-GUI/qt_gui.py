# Irish Dictionary GUI app
# saved as qt_gui.py
# Last edit by Davis Sandefur 16.12.2014

import sys
from PyQt5 import QtCore, QtWidgets, QtGui, QtMultimedia
from dictionary_functions import language_change
from irish_dictionary import irish_dictionary
from audio_grabber import entry_search, related_matches

# TODO: Implement sound support for words that have it.
# TODO: Figure out what the is going on with QtMultimedia and get it to play.

global audio


class Callback():

    def __init__(self):
        self.audio = False  # Set audio as False at first so buttons are greyed out and no audio there

    # Define the Irish version callbacks
    def bearla_callback(self):
        """ Irish version English-language search """
        entry = str(irish_version.entry.text()).lower()
        entries, suggestions, wordlist = irish_dictionary(entry, 'English')
        self.audio = False  # No audio for English words
        for i in entries:
            irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)
            irish_version.text_entry.insertPlainText(i + '\n\n')
        suggestions = language_change(suggestions)
        irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)
        irish_version.text_entry.insertPlainText(suggestions + "\n\nNa focail is déanaí: " + str(wordlist) +
                                                 "\n\n" + 'Níl aon fuaim ar fhocail as Béarla.\n\n')
        irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)

    def gaeilge_callback(self):
        """ Irish version Irish-language search """
        entry = str(irish_version.entry.text()).lower()
        entries, suggestions, wordlist = irish_dictionary(entry, 'Irish')
        related = related_matches(entry)
        self.audio = entry_search(entry)
        for i in entries:
            irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)
            irish_version.text_entry.insertPlainText(i + '\n\n')
        suggestions = language_change(suggestions)
        irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)
        irish_version.text_entry.insertPlainText(suggestions + "\n\nNa focail is déanaí: " + str(wordlist) + "\n\n"
                                                 + '(Fuaim) Torthaí gaolmhara: ' + str(related) + '\n\n')
        irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)

    # Define English version callbacks
    def english_callback(self):
        """ English version English-language search """
        entry = str(english_version.entry.text()).lower()
        entries, suggestions, wordlist = irish_dictionary(entry, 'English')
        self.audio = False  # No audio for English words
        for i in entries:
            english_version.text_entry.moveCursor(QtGui.QTextCursor.End)
            english_version.text_entry.insertPlainText(i + '\n\n')
        english_version.text_entry.moveCursor(QtGui.QTextCursor.End)
        english_version.text_entry.insertPlainText(suggestions + "\n\nRecently used words: " + str(wordlist) +
                                                   "\n\n" + 'No audio for English words.\n\n')
        english_version.text_entry.moveCursor(QtGui.QTextCursor.End)

    def irish_callback(self):
        """ This method is the English version Irish-language search """
        entry = str(english_version.entry.text()).lower()
        entries, suggestions, wordlist = irish_dictionary(entry, 'Irish')
        related = related_matches(entry)
        self.audio = entry_search(entry)
        for i in entries:
            english_version.text_entry.moveCursor(QtGui.QTextCursor.End)
            english_version.text_entry.insertPlainText(i + '\n\n')
        english_version.text_entry.moveCursor(QtGui.QTextCursor.End)
        english_version.text_entry.insertPlainText(suggestions + "\n\nRecently used words: " + str(wordlist) + "\n\n"
                                                   + '(Audio) Related Matches: ' + str(related) + '\n\n')
        english_version.text_entry.moveCursor(QtGui.QTextCursor.End)

    # Define language switching callbacks
    @staticmethod
    def irish_to_english():
        """ This method converts the Irish language version to English """
        irish_version.hide()
        english_version.show()
        irish_version.layout().removeWidget(irish_version.text_entry)
        english_version.layout().addWidget(english_version.text_entry, 2, 0, 24, 8)
        english_version.resize(200, 400)
        english_version.center()

    @staticmethod
    def english_to_irish():
        """ This method converts the English language version to Irish"""
        english_version.hide()
        irish_version.show()
        english_version.layout().removeWidget(english_version.text_entry)
        irish_version.layout().addWidget(irish_version.text_entry, 2, 0, 24, 8)
        irish_version.resize(200, 400)
        irish_version.center()

    @staticmethod
    def munster():
        """ This method plays the Munster recording, if it exists"""
        url = QtCore.QUrl.fromLocalFile("./CanM.mp3")
        content = QtMultimedia.QMediaContent(url)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()



    @staticmethod
    def connacht():
        """ This method plays the Connacht recording if it exists"""

    @staticmethod
    def ulster():
        """ This method plays the Ulster recording, it it exists"""

# Create Irish version widgets


class IrishLabel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """ This class creates the Irish language label, entry box, and version switcher """
        super().__init__(parent)
        self.irish_label = QtWidgets.QLabel("Cuir d'fhocal anseo:")
        self.irish_entry = QtWidgets.QLineEdit()
        self.english_language_button = QtWidgets.QPushButton("English Version")
        self.english_language_button.clicked.connect(lambda: Callback.irish_to_english())


class IrishButtons(QtWidgets.QWidget):
    """ this class creates the Irish language buttons"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.bearla_button = QtWidgets.QPushButton("Béarla")
        self.gaeilge_button = QtWidgets.QPushButton("Gaeilge")

        self.bearla_button.clicked.connect(lambda: Callback.bearla_callback())
        self.gaeilge_button.clicked.connect(lambda: Callback.gaeilge_callback())


# Create English version widgets
class EnglishLabel(QtWidgets.QWidget):
    """ This class Creates English labels"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.english_label = QtWidgets.QLabel("Enter your word here:")
        self.english_entry = QtWidgets.QLineEdit()
        self.irish_language_button = QtWidgets.QPushButton("Leagan Gaeilge")

        self.irish_language_button.clicked.connect(lambda: Callback.english_to_irish())


class EnglishButtons(QtWidgets.QWidget):
    """ This class creates the English version buttons"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.english_button = QtWidgets.QPushButton("English")
        self.irish_button = QtWidgets.QPushButton("Irish")

        self.english_button.clicked.connect(lambda: Callback.english_callback())
        self.irish_button.clicked.connect(lambda: Callback.irish_callback())


class Text(QtWidgets.QWidget):
    """ This class creates the text widget"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.text_entry = QtWidgets.QTextEdit(parent)
        self.text_entry.setReadOnly(True)


class IrishVersion(QtWidgets.QWidget):
    """ This class brings together all the Irish version widgets and
    lays them out in the correct order. Also controls window title and maximize button
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.label = irish_label.irish_label
        self.entry = irish_label.irish_entry
        self.switcher = irish_label.english_language_button
        self.bearla = irish_buttons.bearla_button
        self.gaeilge = irish_buttons.gaeilge_button
        self.text_entry = text.text_entry

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.entry, 0, 1, 1, 4)
        grid.addWidget(self.switcher, 0, 6)
        grid.addWidget(self.bearla, 1, 2)
        grid.addWidget(self.gaeilge, 1, 4)
        self.setLayout(grid)

        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.setWindowTitle("Foclóir")
        self.resize(200, 400)

    def center(self):

        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class EnglishVersion(QtWidgets.QWidget):
    """ This class brings together all the English version widgets and lays them out in the correct
    order. Also controls the English version window title and disables the maximize button
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.label = english_label.english_label
        self.entry = english_label.english_entry
        self.switcher = english_label.irish_language_button
        self.bearla = english_buttons.english_button
        self.gaeilge = english_buttons.irish_button
        self.text_entry = text.text_entry

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.entry, 0, 1, 1, 4)
        grid.addWidget(self.switcher, 0, 6)
        grid.addWidget(self.bearla, 1, 2)
        grid.addWidget(self.gaeilge, 1, 4)
        grid.addWidget(self.text_entry, 2, 0, 24, 8)
        self.setLayout(grid)

        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.setWindowTitle("Breis.focloir.ie Searcher")
        self.resize(200, 400)

    def center(self):

        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

#Callback.munster()
app = QtWidgets.QApplication(sys.argv)
irish_label = IrishLabel()
english_label = EnglishLabel()
irish_buttons = IrishButtons()
english_buttons = EnglishButtons()
text = Text()
irish_version = IrishVersion()
english_version = EnglishVersion()
english_version.show()
english_version.center()
sys.exit(app.exec_())
