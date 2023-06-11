from pytube import YouTube as yt


def Download(link): 
    yt_object = yt(link)
    yt_object = yt_object.streams.get_audio_only()
    try:
        yt_object.download()
    except:
        print("Could not download file")
    print("File downloaded")

link = input("Enter link of the music: \n")
Download(link)
