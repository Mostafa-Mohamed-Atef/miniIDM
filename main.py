import tkinter 
import ttkbootstrap as ttk 
from pytube import YouTube

def Download(url):
    try:
       yt = YouTube(url).streams.get_highest_resolution()
       print(yt.title)
       yt.download()
    #    print(yt.streams)
    except Exception as e:
        print(e)

url = input("import your link: \n")
Download(url)