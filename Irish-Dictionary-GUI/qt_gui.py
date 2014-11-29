import sys
from PyQt4 import QtCore, QtGui
from irish_dictionary import irish_dictionary
from dictionary_classes import StringCleanup, SuggestionsToIrish

# TODO: Implement sound support for words that have it.


class Callback():

    # Define the Irish version callbacks
    @ staticmethod
    def bearla_callback():
        """ English callback method """
        entry = str(irish_version.entry.text()).lower()
        entries, suggestions, wordlist = irish_dictionary(entry, 'English')
        for i in entries:
            irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)
            irish_version.text_entry.insertPlainText(i + '\n\n')
        suggestions = StringCleanup(suggestions).cleanup()
        suggestions = SuggestionsToIrish(suggestions).language_change()
        irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)
        irish_version.text_entry.insertPlainText(suggestions + "\n\nNa focail is déanaí: " + str(wordlist) +
                                                 "\n\n")
        irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)

    @staticmethod
    def gaeilge_callback():
        """ English callback method """
        entry = str(irish_version.entry.text()).lower()
        entries, suggestions, wordlist = irish_dictionary(entry, 'Irish')
        for i in entries:
            irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)
            irish_version.text_entry.insertPlainText(i + '\n\n')
        suggestions = StringCleanup(suggestions).cleanup()
        suggestions = SuggestionsToIrish(suggestions).language_change()
        irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)
        irish_version.text_entry.insertPlainText(suggestions + "\n\nNa focail is déanaí: " + str(wordlist) + "\n\n")
        irish_version.text_entry.moveCursor(QtGui.QTextCursor.End)

    # Define English version callbacks
    @staticmethod
    def english_callback():
        """ English callback method """
        entry = str(english_version.entry.text()).lower()
        entries, suggestions, wordlist = irish_dictionary(entry, 'English')
        for i in entries:
            english_version.text_entry.moveCursor(QtGui.QTextCursor.End)
            english_version.text_entry.insertPlainText(i + '\n\n')
        suggestions = StringCleanup(suggestions).cleanup()
        english_version.text_entry.moveCursor(QtGui.QTextCursor.End)
        english_version.text_entry.insertPlainText(suggestions + "\n\nRecently used words: " + str(wordlist) +
                                                   "\n\n")
        english_version.text_entry.moveCursor(QtGui.QTextCursor.End)

    @staticmethod
    def irish_callback():
        """ English callback method """
        entry = str(english_version.entry.text()).lower()
        entries, suggestions, wordlist = irish_dictionary(entry, 'Irish')
        for i in entries:
            english_version.text_entry.moveCursor(QtGui.QTextCursor.End)
            english_version.text_entry.insertPlainText(i + '\n\n')
        suggestions = StringCleanup(suggestions).cleanup()
        english_version.text_entry.moveCursor(QtGui.QTextCursor.End)
        english_version.text_entry.insertPlainText(suggestions + "\n\nRecently used words: " + str(wordlist) + "\n\n")
        english_version.text_entry.moveCursor(QtGui.QTextCursor.End)

    # Define language switching callbacks
    @staticmethod
    def irish_to_english():
        irish_version.hide()
        english_version.show()
        irish_version.layout().removeWidget(irish_version.text_entry)
        english_version.layout().addWidget(english_version.text_entry, 2, 0, 24, 8)
        english_version.resize(200, 400)
        english_version.center()

    @staticmethod
    def english_to_irish():
        english_version.hide()
        irish_version.show()
        english_version.layout().removeWidget(english_version.text_entry)
        irish_version.layout().addWidget(irish_version.text_entry, 2, 0, 24, 8)
        irish_version.resize(200, 400)
        irish_version.center()


# Create Irish version widgets
class IrishLabel(QtGui.QWidget):
    def __init__(self, parent=None):
        """ This class creates the Irish language label, entry box, and version switcher """
        super().__init__(parent)
        self.irish_label = QtGui.QLabel("Cuir d'fhocal anseo:")
        self.irish_entry = QtGui.QLineEdit()
        self.english_language_button = QtGui.QPushButton("English Version")

        self.english_language_button.clicked.connect(lambda: Callback.irish_to_english())


class IrishButtons(QtGui.QWidget):
    """ this class creates the Irish language buttons"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.bearla_button = QtGui.QPushButton("Béarla")
        self.gaeilge_button = QtGui.QPushButton("Gaeilge")

        self.bearla_button.clicked.connect(lambda: Callback.bearla_callback())
        self.gaeilge_button.clicked.connect(lambda: Callback.gaeilge_callback())


# Create English version widgets
class EnglishLabel(QtGui.QWidget):
    """ This class Creates English labels"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.english_label = QtGui.QLabel("Enter your word here:")
        self.english_entry = QtGui.QLineEdit()
        self.irish_language_button = QtGui.QPushButton("Leagan Gaeilge")

        self.irish_language_button.clicked.connect(lambda: Callback.english_to_irish())


class EnglishButtons(QtGui.QWidget):
    """ This class creates the English version buttons"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.english_button = QtGui.QPushButton("English")
        self.irish_button = QtGui.QPushButton("Irish")

        self.english_button.clicked.connect(lambda: Callback.english_callback())
        self.irish_button.clicked.connect(lambda: Callback.irish_callback())


class Text(QtGui.QWidget):
    """ This class creates the text widget"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.text_entry = QtGui.QTextEdit(parent)
        self.text_entry.setReadOnly(True)


class IrishVersion(QtGui.QWidget):
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

        grid = QtGui.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.entry, 0, 1, 1, 4)
        grid.addWidget(self.switcher, 0, 6)
        grid.addWidget(self.bearla, 1, 2)
        grid.addWidget(self.gaeilge, 1, 4)
        self.setLayout(grid)

        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowTitle("Foclóir")
        self.resize(200, 400)

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class EnglishVersion(QtGui.QWidget):
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

        grid = QtGui.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.entry, 0, 1, 1, 4)
        grid.addWidget(self.switcher, 0, 6)
        grid.addWidget(self.bearla, 1, 2)
        grid.addWidget(self.gaeilge, 1, 4)
        grid.addWidget(self.text_entry, 2, 0, 24, 8)
        self.setLayout(grid)

        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowTitle("Breis.focloir.ie Searcher")
        self.resize(200, 400)

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

app = QtGui.QApplication(sys.argv)
irish_label = IrishLabel()
english_label = EnglishLabel()
irish_buttons = IrishButtons()
english_buttons = EnglishButtons()
text = Text()
irish_version = IrishVersion()
english_version = EnglishVersion()
english_version.show()
english_version.center()
app.exec_()
