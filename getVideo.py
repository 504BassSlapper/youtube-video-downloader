from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_by_resolution("360p")
    try:
        youtubeObject.download()
    except:
        print("an error occured")
    print(youtubeObject.get_file_path() + " downloaded successfully")
    
link= input("Enter link of the video \n")
Download(link)

    