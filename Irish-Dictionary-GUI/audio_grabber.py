# This module will download the audio from breis.focloir.ie/fuaim if it exists
# if not, it will return related matches to search, if they exist.
# Saved as audio_catcher.py
# Created by Davis Sandefur; last updated 13.12.14

""" This module contains the code necessary to download the sound files for a particular word from breis.focloir.ie,
assuming the files exist. It also returns related matches, if they exist. If there is no sound, it returns any related
matches. If neither, it returns None
"""


import urllib.request
import urllib.parse


def entry_search(word):
    """ This function downloads sound for the string <word> if it exists. It also returns related words from the webpage.
    If word exists, it also returns TRUE. If words don't exist, it returns FALSE
    """
    word = urllib.parse.quote_plus(word)
    for i in range(len(word)):
        if word[i] == "+":
            begin_word = word[:i]
            end_word = word[i+1:]
            word = begin_word + '%20' + end_word

    # print(word)  # Test to make sure word is in correct form for URL

    slug_list = ['CanM%2f', 'CanC%2F', 'CanU%2F']
    for i in slug_list:
        url = 'http://breis.focloir.ie/' + i + word + '.mp3'
        print(url)  # Test to check URL
        urllib.request.urlretrieve(url, i+'.mp3')




if __name__ == '__main__':
    entry_search('téigh')
    entry_search('seo a chuaigh thart')