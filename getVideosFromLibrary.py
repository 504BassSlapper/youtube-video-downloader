from pytube import YouTube
from pytube import Playlist
import os
import shutil


def move_files_to_subdirectory(src_dir, dest_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    files = os.listdir(src_dir)
    for file in files:
        if file.endswith(".mp4"):
            new_file_name = os.path.splitext(file)[0] + ".mp3"

            # get source and destination file path before mv
            src_file_path = os.path.join(src_dir, file)
            dest_file_path = os.path.join(dest_dir, new_file_name)
            # performing mv
            try:
                shutil.move(src_file_path, dest_file_path)
                print(
                    f"The file '{src_file_path}' have been renamed and mooved successfully"
                )
            except:
                print(f"could not transfert '{src_file_path}' to '{dest_file_path}'")


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
    move_files_to_subdirectory(".", "mp4")

def DownloadSingleAudio(link):
    yt_object = YouTube(link)
    yt_object = yt_object.streams.get_audio_only()
    try:
        yt_object.download()
    except:
        print("Could not download the audio file using this url")
    move_files_to_subdirectory(".", "mp3")


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
