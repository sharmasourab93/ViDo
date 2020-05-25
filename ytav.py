import os
import pafy
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog


class Downloader:
    
    def __init__(self, root):
        """
            Initializing Downloader Constructor
        """
        self.av, self.stream_button, self.url_text = None, \
                                                     IntVar(), \
                                                     StringVar()
        self.folder_path = ""
        
        # Root Config Setup
        root.title("You Tube Audio Video Downloader")
        root.geometry("980x480")
        style = ttk.Style()
        style.configure("TButton", font="Calibri 18", padding=10)
        style.configure("TEntry", font="Calibri 13", padding=10)
        
        # URL Entry happens here
        
        Label(root, text="Enter URL:").grid(row=0, column=0)
        self.url_entry = Entry(root,
                               width=120,
                               textvariable=self.url_text)
        
        self.url_entry.grid(sticky=E,
                            pady=10,
                            row=0,
                            column=1)
        
        # Choosing/Changing Download folder location
        
        Label(root, text="Download Path:") \
            .grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.download = Entry(root, width=120)
        self.download.grid(sticky=E, padx=1, pady=10, row=1, column=1)
        self.download.insert(0, self.folder_path)
        download_path_button = Button(root, text="Choose Folder")
        download_path_button.grid(row=1, column=2, pady=5)
        download_path_button.config(command=self.open_choose_folder)
        
        # Submit Button to validate url and look for AV quality
        
        self.validate_button = Button(root, text="Validate URL")
        self.validate_button.grid(row=3, column=0, sticky=W, padx=10, pady=10)
        self.validate_button.config(command=self.validate_url)
        
        # Post Validate URL Button Click Preview
        # To Be Added soon
        
        # Choosing Audio or Video Options
        
        self.radio_val = IntVar()
        Label(root, text="Audio or Video") \
            .grid(row=5, column=0, sticky=W)
        radio1 = Radiobutton(root,
                             text="Audio",
                             value=0,
                             variable=self.radio_val) \
            .grid(row=7, column=0, sticky=W, padx=10, pady=10)
        radio2 = Radiobutton(root,
                             text="Video",
                             value=1,
                             variable=self.radio_val) \
            .grid(row=7, column=1, sticky=W, padx=10, pady=10)
        
        get_streams_button = Button(root,
                                    text="Get Available Streams",
                                    command=self.get_streams) \
            .grid(row=7, column=2, sticky=W)
        
        # Download Button Clicked Here
        dwd = Button(root,
                     text="Download",
                     command=self.download_video) \
            .grid(row=8, column=2, rowspan=6, pady=10)
    
    def open_choose_folder(self):
        """ This Method looks into handling the Primary
            working folder where the file is to be downloaded.
        """
        self.folder_path = filedialog\
            .askdirectory(parent=root,
                          initialdir=r'C:/Users/Sourab Sharma/Downloads')
        self.download.delete(0, "end")
        self.download.insert(0, self.folder_path)
        os.chdir(self.folder_path)

    @staticmethod
    def invalid_message(i=1):
        """ Message Box to be displayed on Exception Catch """
        
        if i == 1:
            messagebox.showerror("Invalid URL entered",
                                 "Please enter a valid URL ")
        elif i == 2:
            messagebox.showerror("No URL Found",
                                 "Enter a Video URL to download!")
        else:
            messagebox.showerror("Connectivity Issue",
                                 "No Active connection. Please connect and try again!")

    def get_url(self):
        """ Returns the Entered URL """
        return self.url_text.get()
      
    def validate_url(self):
        """
            This method Validates if this given url is Valid or not.
            Triggered when Validate URL button is clicked.
        """
        try:
            self.av = pafy.new(self.get_url())
            
        except ValueError:
            Downloader.invalid_message()
            
        except OSError:
            Downloader.invalid_message(0)
    
    def get_streams(self):
        """
            Prints All the Available streams on the Interface.
            Triggered when Get All Available streams button is clicked.
        """
        
        Label(root, text="Available Streams").grid(row=8, column=0)
        
        if self.radio_val.get():
            vstreams = list(set(self.av.videostreams))
            for i in range(len(vstreams)):
                Radiobutton(root,
                            text=str(vstreams[i]).replace('video:',
                                                          ''),
                            value=i, variable=self.stream_button)\
                    .grid(row=9+i, column=1,sticky=W,padx=5)
        else:
            audio = list(set(self.av.audiostreams))
            for i in range(len(audio)):
                Radiobutton(root,
                            value=i,
                            text=str(audio[i]).replace('audio:',
                                                       ''),
                            variable=self.stream_button)\
                    .grid(row=9+i, column=0, sticky=W, padx=5)
                
    def download_video(self):
        """
            This method downloads the video from the URL.
            This method is triggered when Download button is clicked.
            This is the last Event to be triggered in the process flow.
        """
        if self.radio_val.get():
            v = self.av.videostreams
            
            try:
                v[self.stream_button.get()]\
                    .download(quiet=True, filepath=self.folder_path)
            except FileExistsError:
                os.rename(v[self.stream_button.get()]
                          .download(quiet=True,
                                    filepath=self.folder_path),
                          os.path.join(self.folder_path,
                                       str(self.av.title)+'1'))
            
            except AttributeError:
                Downloader.invalid_message(2)
        
        else:
            a = self.av.audiostreams
            
            try:
                a[self.stream_button.get()]\
                    .download(quiet=True,
                              filepath=self.folder_path)
                
            except FileExistsError:
                os.rename(a[self.stream_button.get()]
                          .download(quiet=True,
                                    filepath=self.folder_path),
                          os.path.join(self.folder_path,
                                       str(self.av.title)+'1'))
                
            except AttributeError:
                Downloader.invalid_message(2)

    @staticmethod
    def quit_app(event=None):
        """ To Quit the Root Tkinter App. """
        root.quit()
    

if __name__ == '__main__':
    root = Tk()
    d = Downloader(root)
    root.resizable(False, False)
    root.mainloop()
