# cSpell: disable
from tkinter import *
import yt_dlp

def download_video(quality):
    video_url = Imk.get()


    if quality == 'high':
        ydl_opts = {
            'format': 'best',  
        }

    elif quality == 'low':
        ydl_opts = {
            'format': 'worst',  
        }

    elif quality == 'audio':
        ydl_opts = {
            'format': 'bestaudio',  
        }

    print("Downloading...")  
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])  
    print("Download completed successfully!")  

root = Tk()
root.title("Downloader")

label = Label(root, text="Enter YouTube Video URL:")
label.pack(pady=5)

Imk = Entry(root, width=50)
Imk.pack(pady=10)


frame = Frame(root)
frame.pack(pady=10)


high_button = Button(frame, text="High Quality", command=lambda: download_video('high'))
high_button.pack(side=LEFT, pady=5)

low_button = Button(frame, text="Low Quality", command=lambda: download_video('low'))
low_button.pack(side=RIGHT, pady=5)


audio_button = Button(root, text="Audio Only", command=lambda: download_video('audio'))
audio_button.pack(pady=5)


root.mainloop()
