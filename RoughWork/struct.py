class video_var(self,resol, extension, url):
    def __init__(self, resol, extension,url):
        resol=self.resol
        extension=self.extension
        url=self.url
def main():
    my_foos=[]
    my_foos.append(video_var('1280x720','.mp3','http://1234.com'))
    my_foos.append(video_var('720x480','.mp4','http://12345.com'))
    print(my_foos)
    
main()
    
