import tkinter as tk
from pytube import YouTube

root = tk.Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('youtube downloader')

def download():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download("C:/Users/serba/Desktop/YOUTUBE VIDEOS WITH PYTHON")
    tk.Label(root, text="Downloaded", font="arial 15").place(x=100, y=120)
    video.resolution("720p")
tk.Label(root, text="Download Youtube videos!!", font='san-serif 14 bold').pack()
link = tk.StringVar()
tk.Label(root, text="Paste your link here", font='san-serif 15 bold').place(x=150, y=55)
link_enter = tk.Entry(root, width=70, textvariable=link).place(x=30, y=85)

tk.Button(root, text='Download', font='san-serif 16 bold', bg='red', padx=2,command=download).place(x=100, y=150)


root.mainloop()