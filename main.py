from tkinter import *
import tkinter as tk
from pytube import YouTube

def get_video_url():
    url = url_entry.get()
    youtube = YouTube(url)
    video = youtube.streams.first()
    video.download()
    lb1 = Label(root, text='Download Concluido!!!', fg="#fc0366", width=30, bg="#361d2c", borderwidth=1, relief='solid')
    canvas1.create_window(200,200, window=lb1)
    
    
root = tk.Tk()
root.title('Youtube Downloader')
root.iconphoto(False, tk.PhotoImage(file = 'índice.png'))
root.geometry("400x400")
root.resizable(width= False, height = False)
canvas1 = Canvas(root, height=400, width=400, bg="#8f175f")
canvas1.pack()

label1 = Label(root, text='INSIRA A URL ABAIXO:',fg='#fc0366', width=30, bg = "#361d2c", borderwidth=1, relief='solid')
canvas1.create_window(200,100, window= label1)

url_entry = Entry(root)
canvas1.create_window(200,140, window=url_entry)

download_bt= Button(root, text='DOWNLOAD', fg='#fc0366', width=20, bg='#361d2c', borderwidth=1, relief='solid', command= get_video_url)
canvas1.create_window(200,180, window=download_bt)
root.mainloop()