from tkinter import *
import re
from downloader import Download, DownloadSingleVideo, DownloadSingleAudio

def download_url_content(format):
    if format == "Playlist":
        Download(input.get(), isAudio=is_mp3.get())
        label2.config(text="Downloaded !")
        button.configure()     
    elif format == "Video": 
   
        if is_mp3.get() == "y":
            DownloadSingleAudio(input.get())
        else:
            DownloadSingleVideo(input.get())
  
    else:
        label2.config(text="Not a youtube video") 
       
def on_entry_click(event):
    """Function to handle the click event on the entry widget"""
    if input.get() == "Enter text here":
        input.delete(0, END)
        input.config(foreground='white')

def on_focus_out(event):
    """Function to handle the focus out event on the entry widget"""
    if input.get() == "":
        input.insert(0, "Enter text here")
        input.config(foreground='gray')
        window.focus_set()
        
def on_root_click(event):
    """Function to handle the click event outside the entry widget"""
    if input.get() == "":
        input.focus_set()
        input.insert(0, "Enter text here")
        input.config(foreground='gray')
        window.focus_set()


def on_close():
    # Perform any necessary cleanup or saving operations here
    window.destroy()


def check_youtube_url(url):
    playlist_regex = r"youtube\.com/playlist"
    video_regex = r"youtube\.com/watch\?v="

    if re.search(playlist_regex, url):
        return "Playlist"
    elif re.search(video_regex, url):
        return "Video"
    else:
        return "Unknown"

def on_click_button():
    button.configure(state="disabled" , bg="gray")
    video_checker = check_youtube_url(input.get())
    label2.config(text="Downloading ...")
    label2.pack()
    if input.get().strip():
        label2.config(text=f"this url is {video_checker}")
        download_url_content(video_checker)
        button.configure(state="normal" )
        
 

window = Tk()
is_mp3 = StringVar()
window.title("tkinter window")
window.minsize(500, 500)
window.config(padx=100, pady=50)
label = Label(text="Youtube video downloader", font=("Arial", 40, "bold italic"))
label.pack()
label.config(pady=100)

label2 = Label(text="please provide url of the video or the playlist")
label2.pack()


input = Entry(width=100, fg="gray", background="black")

input.insert(0, "Enter text here")
input.bind('<FocusIn>', on_entry_click)
input.bind('<FocusOut>', on_focus_out)
# Bind click event outside the entry widget to the root window
window.bind('<Button-1>', on_root_click)
input.pack()

radio_btn1 = Radiobutton(window, text="mp3", variable=is_mp3, value="y")
radio_btn1.pack()
radio_btn2 = Radiobutton(window, text="mp4", variable=is_mp3, value="n")
radio_btn2.pack()
is_mp3.set("y")

button = Button(text="Download")
button.configure(background="blue")

button.configure(command=on_click_button)
button.pack()
# Configure the "WM_DELETE_WINDOW" event to call the on_close function


window.protocol("WM_DELETE_WINDOW", on_close)

window.mainloop()

