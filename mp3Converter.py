
from __future__ import unicode_literals
from youtube_dl import YoutubeDL
import sys
from tkinter import filedialog
import os
import tkinter


class MainProgram:
    def __init__(self):
        self.root = tkinter.Tk()
        self.directoryUser = os.getcwd()

        self.label_url = tkinter.Label(self.root, text="URL: ")
        self.entry = tkinter.Entry(self.root)
        self.label_dic = tkinter.Label(self.root, text="Current Directory: {}".format(self.directoryUser))
        self.button_dic = tkinter.Button(self.root, text='Change Directory',command=self.ChangeDirectoryByUser)
        self.buttonDownload = tkinter.Button(self.root, text="Download", command=self.DownloadVideo)
        
        self.entry.grid(row=0, column=1)
        self.label_url.grid(row=0, column=0)
        self.button_dic.grid(row=1, column=1)
        self.label_dic.grid(row=1, column=0)
        self.buttonDownload.grid(row=2)

        self.root.mainloop()

    def ChangeDirectoryByUser(self):
        self.directoryUser = filedialog.askdirectory()
        self.label_dic["text"] = self.directoryUser
    
    def __checkURL(self, url):
        newUrl = ""
        i = 0   
        for letter in url:
            if letter == "&":
                newUrl = url[:i]
                return newUrl
            i = i + 1
        return newUrl

    def DownloadVideo(self):
        url = self.__checkURL(self.entry.get())
        print(url)
        if url and self.directoryUser:
            ydl_opts = {'format': 'bestaudio/best','outtmpl': '{}/%(title)s.%(ext)s'.format(self.directoryUser),'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}],}
            #info = None
        
            with YoutubeDL(ydl_opts) as ydl:
                #info = ydl.extract_info(url, download=False)
                ydl.download([url])

            #video_title = info.get("title")
            #video_rating = info.get("average_rating")

            print("Finished...")

mp = MainProgram()

input("Finished...")