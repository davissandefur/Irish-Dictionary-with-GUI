# Irish Dictionary GUI app
# saved as qt_gui.py
# Last edit by Davis Sandefur 16.12.2014

import sys, os
from PyQt5 import QtCore, QtWidgets, QtGui, QtMultimedia
from dictionary_functions import language_change
from irish_dictionary import irish_dictionary
from audio_grabber import entry_search, related_matches

# TODO: Implement sound support for words that have it.
# TODO: Figure out what the is going on with QtMultimedia and get it to play.


class Callback():

    # Define the Irish version callbacks
    @staticmethod
    def bearla_callback():
        """ Irish version English-language search """
        entry = str(irish_version.entry.text()).lower()
        entries, suggestions, wordlist = irish_dictionary(entry, 'English')
        for i in entries:
            irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)
            irish_version.text_entry.insertPlainText(i + '\n\n')
        suggestions = language_change(suggestions)
        irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)
        irish_version.text_entry.insertPlainText(suggestions + "\n\nNa focail is déanaí: " + str(wordlist) +
                                                 "\n\n" + 'Níl aon fuaim ar fhocail as Béarla.\n\n')
        irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)

    @staticmethod
    def gaeilge_callback():
        """ Irish version Irish-language search """
        entry = str(irish_version.entry.text()).lower()
        entries, suggestions, wordlist = irish_dictionary(entry, 'Irish')
        related = related_matches(entry)
        for i in entries:
            irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)
            irish_version.text_entry.insertPlainText(i + '\n\n')
        suggestions = language_change(suggestions)
        irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)
        irish_version.text_entry.insertPlainText(suggestions + "\n\nNa focail is déanaí: " + str(wordlist) + "\n\n"
                                                 + '(Fuaim) Torthaí gaolmhara: ' + str(related) + '\n\n')
        irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)
        return entry_search(entry)

    # Define English version callbacks
    @staticmethod
    def english_callback():
        """ English version English-language search """
        entry = str(english_version.entry.text()).lower()
        entries, suggestions, wordlist = irish_dictionary(entry, 'English')
        for i in entries:
            english_version.text_entry.moveCursor(QtGui.QTextCursor.End)
            english_version.text_entry.insertPlainText(i + '\n\n')
        english_version.text_entry.moveCursor(QtGui.QTextCursor.End)
        english_version.text_entry.insertPlainText(suggestions + "\n\nRecently used words: " + str(wordlist) +
                                                   "\n\n" + 'No audio for English words.\n\n')
        english_version.text_entry.moveCursor(QtGui.QTextCursor.End)

    @staticmethod
    def irish_callback():
        """ This method is the English version Irish-language search """
        entry = str(english_version.entry.text()).lower()
        entries, suggestions, wordlist = irish_dictionary(entry, 'Irish')
        related = related_matches(entry)
        for i in entries:
            english_version.text_entry.moveCursor(QtGui.QTextCursor.End)
            english_version.text_entry.insertPlainText(i + '\n\n')
        english_version.text_entry.moveCursor(QtGui.QTextCursor.End)
        english_version.text_entry.insertPlainText(suggestions + "\n\nRecently used words: " + str(wordlist) + "\n\n"
                                                   + '(Audio) Related Matches: ' + str(related) + '\n\n')
        english_version.text_entry.moveCursor(QtGui.QTextCursor.End)
        return entry_search(entry)

    # Define language switching callbacks
    @staticmethod
    def irish_to_english():
        """ This method converts the Irish language version to English """
        irish_version.hide()
        english_version.show()
        irish_version.layout().removeWidget(irish_version.text_entry)
        english_version.layout().addWidget(english_version.text_entry, 3, 0, 24, 8)
        english_version.resize(200, 400)
        english_version.center()

    @staticmethod
    def english_to_irish():
        """ This method converts the English language version to Irish"""
        english_version.hide()
        irish_version.show()
        english_version.layout().removeWidget(english_version.text_entry)
        irish_version.layout().addWidget(irish_version.text_entry, 3, 0, 24, 8)
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
            player.stateChanged()
            del player



    @staticmethod
    def connacht():
        """ This method plays the Connacht recording if it exists"""
        url = QtCore.QUrl.fromLocalFile("./CanC.mp3")
        content = QtMultimedia.QMediaContent(url)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()

    @staticmethod
    def ulster():
        """ This method plays the Ulster recording, it it exists"""
        url = QtCore.QUrl.fromLocalFile("./CanU.mp3")
        content = QtMultimedia.QMediaContent(url)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()
        player.stateChanged()


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

        # Set buttons and enabled status
        self.bearla_button = QtWidgets.QPushButton("Béarla")
        self.gaeilge_button = QtWidgets.QPushButton("Gaeilge")
        self.connacht_button = QtWidgets.QPushButton("Cúige Chonnacht")
        self.ulster_button = QtWidgets.QPushButton("Cúige Uladh")
        self.munster_button = QtWidgets.QPushButton("Cúige Mhumhan")
        self.connacht_button.setEnabled(False)
        self.ulster_button.setEnabled(False)
        self.munster_button.setEnabled(False)

        # Set callbacks
        self.bearla_button.clicked.connect(lambda: self.audio_english())
        self.gaeilge_button.clicked.connect(lambda: self.audio_check())
        self.munster_button.clicked.connect(lambda: Callback.munster())
        self.connacht_button.clicked.connect(lambda: Callback.connacht())
        self.ulster_button.clicked.connect(lambda: Callback.ulster())

    def audio_english(self):
        Callback.bearla_callback()
        self.ulster_button.setEnabled(False)
        self.connacht_button.setEnabled(False)
        self.munster_button.setEnabled(False)

    def audio_check(self):
        audio = Callback.gaeilge_callback()
        if audio:
            self.ulster_button.setEnabled(True)
            self.connacht_button.setEnabled(True)
            self.munster_button.setEnabled(True)
        if not audio:
            self.ulster_button.setEnabled(False)
            self.connacht_button.setEnabled(False)
            self.munster_button.setEnabled(False)


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

        # Define buttons
        self.english_button = QtWidgets.QPushButton("English")
        self.irish_button = QtWidgets.QPushButton("Irish")
        self.audio = False  # Initial audio setting
        self.ulster_button = QtWidgets.QPushButton("Ulster Dialect")
        self.connacht_button = QtWidgets.QPushButton("Connacht Dialect")
        self.munster_button = QtWidgets.QPushButton("Munster Dialect")

        # Define Callback procedures
        self.english_button.clicked.connect(lambda: self.audio_english())
        self.irish_button.clicked.connect(lambda: self.audio_check())
        self.munster_button.clicked.connect(lambda: Callback.munster())
        self.connacht_button.clicked.connect(lambda: Callback.connacht())
        self.ulster_button.clicked.connect(lambda: Callback.ulster())

        # Initial disabling of audio buttons
        self.ulster_button.setEnabled(False)
        self.munster_button.setEnabled(False)
        self.connacht_button.setEnabled(False)

    def audio_english(self):
        os.remove('./CanM.mp3')
        os.remove('./CanC.mp3')
        os.remove('./CanU.mp3')
        Callback.english_callback()
        self.ulster_button.setEnabled(False)
        self.connacht_button.setEnabled(False)
        self.munster_button.setEnabled(False)

    def audio_check(self):
        self.audio = Callback.irish_callback()
        if self.audio:
            self.ulster_button.setEnabled(True)
            self.connacht_button.setEnabled(True)
            self.munster_button.setEnabled(True)
        if not self.audio:
            self.ulster_button.setEnabled(False)
            self.connacht_button.setEnabled(False)
            self.munster_button.setEnabled(False)


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
        self.ulster = irish_buttons.ulster_button
        self.connacht = irish_buttons.connacht_button
        self.munster = irish_buttons.munster_button

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.entry, 0, 1, 1, 4)
        grid.addWidget(self.switcher, 0, 6)
        grid.addWidget(self.bearla, 1, 2)
        grid.addWidget(self.gaeilge, 1, 4)
        grid.addWidget(self.ulster, 2, 2)
        grid.addWidget(self.connacht, 2, 3)
        grid.addWidget(self.munster, 2, 4)
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
        self.connacht = english_buttons.connacht_button
        self.ulster = english_buttons.ulster_button
        self.munster = english_buttons.munster_button

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.entry, 0, 1, 1, 4)
        grid.addWidget(self.switcher, 0, 6)
        grid.addWidget(self.bearla, 1, 2)
        grid.addWidget(self.gaeilge, 1, 4)
        grid.addWidget(self.ulster, 2, 2)
        grid.addWidget(self.connacht, 2, 3)
        grid.addWidget(self.munster, 2, 4)
        grid.addWidget(self.text_entry, 3, 0, 24, 8)
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


