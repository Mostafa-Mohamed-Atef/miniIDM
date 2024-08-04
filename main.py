import tkinter 
import ttkbootstrap as ttk 
from pytubefix import YouTube

def Download(url):
    try:
       yt = YouTube(url)
       yd = yt.streams.get_highest_resolution()
       print(yt.title)
       yd.download("/home/mostafa/programming/python/miniIDM/")
       print('completed')
    except Exception as e:
        print(e)

url = input("import your link: \n")
Download(url)