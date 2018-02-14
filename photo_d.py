# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 23:25:20 2018

@author: Jayapraveen
"""

import urllib
import os

os.system('mkdir folder') # creates a folder where the photos are to be downloaded
os.chdir ('folder')     # changes directory to that folder

i=0  # initial counter
errorCount=0  #  error counter to measure 404 error(page not found)


def download_photo(url,photo):

    image=urllib.URLopener()
    image.retrieve(url,photo)  # download the photo at URL

n=0001  #initial photo number
for x in range (0,500):  # 500 photos to be downloaded
    
    try:
   
            Number=str(n)  # string containing the number
            photo=str(Number+".jpg")  # string containing the file name
            url=str("URL"+photo)  # The URL for the photo
            download_photo(url,photo)  # uses the function defined above to download the photo
            print url
            n=n+1  # increments the counter to go to the next photo must be before the download in case the download raises an exception
            i+=1
        
            
    except IOError:  # urllib raises an IOError for a 404 error, when the comic doesn't exist
        errorCount+=1  # add one to the error count
        if errorCount>10:  # if more than three errors occur during downloading, quit the program
            break
        else:
            print str("Photo"+ ' ' + str(i) + ' ' + "does not exist")  # otherwise say that the certain photo doesn't exist

print "all photos downloaded"  # prints if all photos are downloaded
