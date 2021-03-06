# This module will download the audio from teanglannie/fuaim if it exists
# if not, it will return related matches to search, if they exist.
# Saved as audio_catcher.py
# Created by Davis Sandefur; last updated 15.07.2015

""" This module contains the code necessary to download the sound files for a particular word from teanglann.ie,
assuming the files exist. It also returns related matches, if they exist. If there is no sound, it returns any related
matches. If neither, it returns None
"""

from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import urllib.parse
import os
import sys


def entry_search(word):
    """ This function downloads sound for the string <word> if it exists.  If sound exists, it also returns TRUE. If sound
    doesn't exist, it returns FALSE, which will be used by the GUI to enable/disable the audio buttons.
    """

    word = urllib.parse.quote_plus(word)
    if "+" in word:
        for i in range(len(word) + 1):
            if word[i] == "+":
                begin_word = word[:i]
                end_word = word[i+1:]
                word = begin_word + '%20' + end_word

    slug_list = ['CanM', 'CanC', 'CanU']
    for i in slug_list:
        url = 'http://teanglann.ie/' + i + '%2F' + word + '.mp3'
        try:
            if sys.platform == "win32":
                urllib.request.urlretrieve(url, os.getenv('APPDATA')+'/'+i+'.mp3')
            else:
                urllib.request.urlretrieve(url, i+'.mp3')
        except urllib.error.HTTPError:
            return False

    return True


def related_matches(word):
    """ This function returns the related matches of a string (word) as given by teanglann.ie/en/fuaim/<word>. It
    returns them in list form, with nothing but spaces and the text.
    """

    word = urllib.parse.quote_plus(word)
    for i in range(len(word)):
        if word[i] == "+":
            begin_word = word[:i]
            end_word = word[i+1:]
            word = begin_word + '_' + end_word
    response = urllib.request.urlopen('http://teanglann.ie/en/fuaim/'+word)
    html = response.read()
    soup = BeautifulSoup(html)
    entry = soup.findAll('div', class_='partial')  # HTML of the entries
    entries = []
    for i in entry:
        entries.append(i.get_text()[:-2])  # [:-2] to remove separate used by the website, since it's not needed
    return entries


if __name__ == '__main__':
    print(entry_search('téigh'))
    print(entry_search('seo a chuaigh thart'))
    print(entry_search(('téigh in éag diaidh ar ndiaidh')))
    print(entry_search('hello'))
    print(related_matches('téigh'))
    print(related_matches('seo a chuaigh thart'))
    print(related_matches('téigh in éag diaidh ar ndiaidh'))