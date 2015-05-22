# coding: utf-8

__author__ = 'Davis Sandefur'

# This file contains unittests for the functions created.
# Davis Sandefur; 22.5.2015

import unittest

from dictionary_functions import word_store, entry_lookup, entry_cleanup, string_cleanup, language_change


def word_store_t():
        word_store_test = []
        for i in range(6):
            if i != 5:
                word_list = word_store("hello", word_store_test)
            elif i == 5:
                word_list = word_store("goodbye", word_store_test)
        return word_list


def english_search():
    entry, suggestion, form_of = entry_lookup("hello", "English", 'english')  # Returns HTML markers
    clean_entry = entry_cleanup(entry)
    suggestions = string_cleanup(entry_cleanup(suggestion))

    return clean_entry, suggestions, form_of

def irish_search():
    entry, suggestion, form_of = entry_lookup("gnóthach", "irish", 'gaeilge')  # Returns HTML markers
    clean_entry = entry_cleanup(entry)
    suggestions = string_cleanup(entry_cleanup(suggestion))

    return clean_entry, suggestions, form_of

def irish_search2():
    entry, suggestion, form_of = entry_lookup("atá", "irish", 'gaeilge')  # Returns HTML markers

    return string_cleanup(entry_cleanup(form_of))

class Test(unittest.TestCase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.entry, self.suggestion, self.form = english_search()
        self.entry2, self.suggestion2, self.form2 = irish_search()


    def test1(self):
        """
        Tests word_store function
        """
        self.assertEqual(['goodbye', 'hello', 'hello', 'hello', 'hello'], word_store_t())

    def test2(self):
        """
        This tests the searching for an English word (hello), and the cleaning up of HTML
        """
        self.assertEqual(['\nhello, int. a (Calling attention)   Hello there, wake up! hóigh, a ghiolla úd! bog thú '
                          'féin!  b (On the telephone) Haló!  c (Indicating surprise)   Hello, is that you? maise, an '
                          'bhfuil tú ann?  d (Greeting) Dia dhuit!  \n'], self.entry)

    def test3(self):
        """
        This tests the cleanup of whitespace around the suggestions using string_cleanup
        """
        self.assertEqual("Similar words: hallo · hell · hullo · 'cello · ell", self.suggestion)

    def test4(self):
        """
        This tests the form_of, which should return None for English words
        """
        self.assertEqual(None, self.form)

    def test5(self):
        """
        This test checks to make sure the 'Similar words" portion of suggestions is changed by the language_change
        function
        """
        self.assertEqual("Focail chosúla: allo · hell · hullo · 'cello · ell", language_change(self.suggestion))

    def test6(self):
        """
        This test checks to make sure Irish entry is parsed correctly
        """
        self.assertEqual(["gnóthach, a1. 1. Busy. Bheith ~ i gceann ruda, to be busy doing  sth. Duine a choinneáil ~, "
                          "to keep s.o. occupied. Lá ~, busy  day. 2. Officious. Nach ~ an mhaise duit é? Aren't you a "
                          " busybody?"], self.entry2)

    def test7(self):
        """
        This test checks Irish suggestion clean-up
        """
        self.assertEqual("Focail chosúla: glóthach · gnáthach · gnóthacht · gnóthadh · gaothach", self.suggestion2)

    def test8(self):
        """
        This test checks form_of for an Irish word that isn't a form of something
        """

        self.assertEqual(None, self.form2)

    def test9(self):
        """
        This test checks form_of for an Irish word that -is- a form of something
        """
        self.assertEqual("Seans gur foirm é atá de: bí » · at »", irish_search2())


if __name__ == "__main__":
    unittest.main()
