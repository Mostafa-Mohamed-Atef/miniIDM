from pytubefix import YouTube
from tqdm import tqdm

progress_bar = None
def download(url):
    global progress_bar
    try:
       yd = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
       print(yt.title)
       print(yd)
       x = input("which stream \n")
       progress_bar = tqdm(total=yd.filesize, unit='0', unit_scale=True, desc="Downloading")
       yd.download(path)
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
path = input("path: \n")
# path = "/home/mostafa/Downloads"
yt = YouTube(url, on_progress_callback=progress)
download(url)