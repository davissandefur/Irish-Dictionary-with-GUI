# This module will download the audio from breis.focloir.ie/fuaim if it exists
# if not, it will return related matches to search, if they exist. 
# Saved as audio_catcher.py
# Created by Davis Sandefur; last updated 13.12.14

""" This module contains the code necessary to download the sound files for a particulary word from breis.focloir.ie/fuaim/<word>, if it exists. It also returns related matches, ifthey exist. If there is no sound, it only returns related matches if they exist. """

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def entry_search(word):
	""" This function searches breis.focloir.ie/fuaim/<word> for the sound files associated with <word> 
	and returns them and similar words if they exist. If they don't, they return similar words. If neither	      exists, it returns that as well. """


	url = 'http://breis.focloir.ie/CanC%2F' + word + '.mp3'
	print(url)
	urllib.request.urlretrieve(url, word+'.mp3')


if __name__ == '__main__':
	entry_search('téigh')
	entry_search('seo a chuaigh thart')
	

