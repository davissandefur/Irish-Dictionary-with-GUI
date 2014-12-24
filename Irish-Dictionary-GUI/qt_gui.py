# Irish Dictionary GUI app
# saved as qt_gui.py
# Last edit by Davis Sandefur 24.12.2014

import sys
from PyQt5 import QtCore, QtWidgets, QtGui, QtMultimedia
from irish_dictionary import irish_dictionary
from audio_grabber import entry_search, related_matches


# Create the widgets used by both versions
class Text(QtWidgets.QWidget):
    """ This class creates the text widget"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.text_entry = QtWidgets.QTextEdit(parent)
        self.text_entry.setReadOnly(True)


# Create Irish version widgets
class IrishLabel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """ This class creates the Irish language label, entry box, and version switcher """
        super().__init__(parent)
        self.irish_label = QtWidgets.QLabel("Cuir d'fhocal anseo:")
        self.irish_entry = QtWidgets.QLineEdit()
        self.english_language_button = QtWidgets.QPushButton("English Version")
        self.english_language_button.clicked.connect(lambda: self.irish_to_english())

    @staticmethod
    def irish_to_english():
        """ This method converts the Irish language version to English """
        irish_version.hide()
        english_version.show()
        irish_version.layout().removeWidget(irish_version.text_entry)
        english_version.layout().addWidget(english_version.text_entry, 3, 0, 24, 8)
        english_version.resize(200, 400)
        english_version.center()


class IrishButtons(IrishLabel):
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
        self.bearla_button.clicked.connect(lambda: self.audio_check('English'))
        self.gaeilge_button.clicked.connect(lambda: self.audio_check('Irish'))
        self.munster_button.clicked.connect(lambda: self.play_audio('Munster'))
        self.connacht_button.clicked.connect(lambda: self.play_audio('Connacht'))
        self.ulster_button.clicked.connect(lambda: self.play_audio('Ulster'))

    def audio_check(self, language):
        audio = self.callback(language)
        if audio:
            self.ulster_button.setEnabled(True)
            self.connacht_button.setEnabled(True)
            self.munster_button.setEnabled(True)
        if not audio:
            self.ulster_button.setEnabled(False)
            self.connacht_button.setEnabled(False)
            self.munster_button.setEnabled(False)

    def callback(self, language):
        """ Irish version English-language search """
        entry = str(self.irish_entry.text()).lower()
        entries, suggestions, wordlist, grammatical = irish_dictionary(entry, language, 'gaeilge')
        audio_exists = entry_search(entry)
        if audio_exists:
            related = related_matches(entry)
        else:
            related = 'Tada'
        if grammatical is not None:
            self.text_entry.moveCursor(QtGui.QTextCursor.End)
            self.text_entry.insertPlainText(grammatical + '\n\n')
        for i in entries:
            self.text_entry.moveCursor(QtGui.QTextCursor.End)
            self.text_entry.insertPlainText(i + '\n\n')
        self.text_entry.moveCursor(QtGui.QTextCursor.End)
        self.text_entry.insertPlainText(suggestions + "\n\nNa focail is déanaí: " + str(wordlist) +
                                        "\n\n" + '(Fuaim) Torthaí gaolmhara:' + str(related) + '\n\n')
        self.text_entry.moveCursor(QtGui.QTextCursor.End)
        return audio_exists

    @staticmethod
    def play_audio(dialect):
        file_names = {'Munster': './CanM.mp3', 'Connacht': './CanC.mp3', 'Ulster': './CanU.mp3'}
        url = QtCore.QUrl.fromLocalFile(file_names[dialect])
        content = QtMultimedia.QMediaContent(url)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()
        player.stateChanged.connect(lambda: player.disconnect())


class IrishVersion(IrishButtons, Text):
    """ This class brings together all the Irish version widgets and
    lays them out in the correct order. Also controls window title and maximize button
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.irish_label, 0, 0)
        grid.addWidget(self.irish_entry, 0, 1, 1, 4)
        grid.addWidget(self.english_language_button, 0, 6)
        grid.addWidget(self.bearla_button, 1, 2)
        grid.addWidget(self.gaeilge_button, 1, 4)
        grid.addWidget(self.ulster_button, 2, 2)
        grid.addWidget(self.connacht_button, 2, 3)
        grid.addWidget(self.munster_button, 2, 4)
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


# Create English version widgets
class EnglishLabel(QtWidgets.QWidget):
    """ This class Creates English labels"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.english_label = QtWidgets.QLabel("Enter your word here:")
        self.english_entry = QtWidgets.QLineEdit()
        self.irish_language_button = QtWidgets.QPushButton("Leagan Gaeilge")
        self.irish_language_button.clicked.connect(lambda: self.english_to_irish())

    @staticmethod
    def english_to_irish():
        """ This method converts the English language version to Irish"""
        english_version.hide()
        global irish_version
        irish_version = IrishVersion()
        irish_version.show()
        english_version.layout().removeWidget(english_version.text_entry)
        irish_version.layout().addWidget(irish_version.text_entry, 3, 0, 24, 8)
        irish_version.resize(200, 400)
        irish_version.center()


class EnglishButtons(EnglishLabel):
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
        self.english_button.clicked.connect(lambda: self.audio_check("English"))
        self.irish_button.clicked.connect(lambda: self.audio_check('Irish'))
        self.munster_button.clicked.connect(lambda: self.play_audio('Munster'))
        self.connacht_button.clicked.connect(lambda: self.play_audio('Connacht'))
        self.ulster_button.clicked.connect(lambda: self.play_audio('Ulster'))

        # Initial disabling of audio buttons
        self.ulster_button.setEnabled(False)
        self.munster_button.setEnabled(False)
        self.connacht_button.setEnabled(False)

    def audio_check(self, language):
        """ Runs callback which prints all entries, suggestions, grammatical forms, etc. Callback also determines if
        an audio recording exists for the word in <language>. If it doesn't, it disables audio buttons. If audio exists,
        it enables buttons.
        """
        self.audio = self.callback(language)
        if self.audio:
            self.ulster_button.setEnabled(True)
            self.connacht_button.setEnabled(True)
            self.munster_button.setEnabled(True)
        if not self.audio:
            self.ulster_button.setEnabled(False)
            self.connacht_button.setEnabled(False)
            self.munster_button.setEnabled(False)

    def callback(self, language):
        """ Callback function that prints entries, suggestions, etc. and returns a boolean for whether the word(s)
         contain(s) audio."""
        entry = str(self.english_entry.text()).lower()
        entries, suggestions, wordlist, grammatical = irish_dictionary(entry, language, 'english')
        audio_exists = entry_search(entry)
        if audio_exists:
            related = related_matches(entry)
        else:
            related = 'None'
        if grammatical is not None:
            self.text_entry.moveCursor(QtGui.QTextCursor.End)
            self.text_entry.insertPlainText(grammatical + '\n\n')
        for i in entries:
            self.text_entry.moveCursor(QtGui.QTextCursor.End)
            self.text_entry.insertPlainText(i + '\n\n')
        self.text_entry.moveCursor(QtGui.QTextCursor.End)
        self.text_entry.insertPlainText(suggestions + "\n\nRecently used words: " + str(wordlist) +
                                        "\n\n" + 'Related Audio Matches: ' + str(related) + '\n\n')
        self.text_entry.moveCursor(QtGui.QTextCursor.End)
        return audio_exists

    @staticmethod
    def play_audio(dialect):
        file_names = {'Munster': './CanM.mp3', 'Connacht': './CanC.mp3', 'Ulster': './CanU.mp3'}
        url = QtCore.QUrl.fromLocalFile(file_names[dialect])
        content = QtMultimedia.QMediaContent(url)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()
        player.stateChanged.connect(lambda: player.disconnect())


class EnglishVersion(EnglishButtons, Text):
    """ This class brings together all the English version widgets and lays them out in the correct
    order. Also controls the English version window title and disables the maximize button
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.english_label, 0, 0)
        grid.addWidget(self.english_entry, 0, 1, 1, 4)
        grid.addWidget(self.irish_language_button, 0, 6)
        grid.addWidget(self.english_button, 1, 2)
        grid.addWidget(self.irish_button, 1, 4)
        grid.addWidget(self.ulster_button, 2, 2)
        grid.addWidget(self.connacht_button, 2, 3)
        grid.addWidget(self.munster_button, 2, 4)
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


def main():
    app = QtWidgets.QApplication(sys.argv)
    global english_version
    english_version = EnglishVersion()
    english_version.show()
    english_version.center()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()