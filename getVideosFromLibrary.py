from pytube import YouTube
from pytube import Playlist


def DownloadSingleVideo(link):
    """_summary_
    this function download a single
    video unsing a link as input
    """
    yt_object = YouTube(link)
    try:
        stream = yt_object.streams.get_by_resolution("360p")
        stream.download()
    except Exception as e:
        print("Could not download Video using this link \n" + link)
        print("an exception occured, maybe this video is not available: \n" + str(e))


def DownloadSingleAudio(link):
    yt_object = YouTube(link)
    yt_object = yt_object.streams.get_audio_only()
    try:
        yt_object.download()
    except:
        print("Could not download the audio file using this url")


def logger(playlist, counter):
    print(counter * "=" + ">")
    print(f"{counter} / {len(playlist)} downloaded")


def Download(link, isVideo):
    """Download

    Args:
        link (string): link of the playlist to download
        isVideo (bool): Download as videos = true / as audios = false
    """
    playlist = Playlist(link)
    counter = 0
    if len(playlist) != 0:
        for url in playlist:
            counter += 1
            if isVideo.lower().strip() == "n":
                DownloadSingleVideo(url)
                logger(playlist, counter)
            else:
                DownloadSingleAudio(url)
            
        print("All playlist videos have been downloaded")
    else:
        print("No youtube video found")


link = input("Please provide the playlist url \n")
isVideo = input("Is this an audio playlist: (y/n) \n")
Download(link, isVideo)
