import tkinter 
from pytube import *

def Download(url):
    try:
       yt = YouTube(url).streams.first().download()
       print(yt.title)
       print(yt.streams.filter(file_extension='mp4'))
    except:
        print("didn't work")

url = input("import your link: \n")
Download(url)