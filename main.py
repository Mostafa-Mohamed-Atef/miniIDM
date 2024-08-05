from pytubefix import YouTube
from tqdm import tqdm

progress_bar = None
def download(url):
    global progress_bar
    try:
       yd = yt.streams.get_highest_resolution()
       print(yt.title)
       progress_bar = tqdm(total=yd.filesize, unit='0', unit_scale=True, desc="Progress")
       yd.download("/home/mostafa/programming/python/miniIDM/")
       progress_bar.close()
       print('completed')
    except Exception as e:
        print(e)
def progress(stream, chunk, bytes_remaining):
    global progress_bar
    file_size = stream.filesize
    bytes_downloaded = file_size - bytes_remaining
    progress_bar.update(len(chunk))

url = input("import your link: \n")
yt = YouTube(url, on_progress_callback=progress)
download(url)