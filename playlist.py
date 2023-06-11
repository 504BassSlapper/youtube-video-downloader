from pytube import Playlist

playlist = Playlist("https://www.youtube.com/watch?v=jr7LSdDLBN8&list=PLjkLvXETDCHA5UVMDW8RthFtn_hygpN5C")
print("size of playliste" + str(len(playlist)))