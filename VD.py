# YouTube Video Audio Downloader
import pafy
import tkinter as tk
class video_var(self,resol, extension, url):
    def __init__(self):
        self.resol=resol
        self.extension=extension
        self.url=url
class Downloader(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        master.minsize(width=666, height=666)
        master.minsize(width=666, height=666)
        #frame=tk.Tk()
        #frame.resizable(width=False, height=False)
        self.pack()

    def first_box(self):
        enter_url=tk.Entry(self).grid(row=0)
        url=enter_url.get()
        video=pafy.new(url)
        label=tk.Label(self,text='Videos').grid(row=1, column=0)
        Cvideo=tk.RADIOBUTTON(command=video_streams).grid(row=1, column=1)
        label=tk.Label(self,text='Audio').grid(row=2, column=0)
        Cvideo=tk.RADIOBUTTON(command=audio_streams).grid(row=2, column=1)
    def audio_streams(self):
        audio=video.audiostreams
        audio_array=[]
        for l in audio:
            if(l.extension=='m4a'):
                audio_array.append(l.url)
        

    def video_streams(self):
        streams=video.streams
        video_array=[]
        video_resol=[]
        for s in streams:
            if(s.resolution =='1280x720' or s.resolution =='640x360'):
                video_resol.append(s.resolution)
                video_array.append[]
        

        
def main():
    
