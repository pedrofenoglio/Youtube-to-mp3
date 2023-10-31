from pytube import Playlist

# URL of the YouTube playlist
playlist_url = str(input("Paste a Youtube playlist link: "))
# playlist_url = "https://www.youtube.com/watch?v=KWfXo5emR8w&list=PLvLB0DOy9-LdCFQPgiizgdLcd0Vxfb4h1"

# Create a Playlist object
playlist = Playlist(playlist_url)

# Extract and print the links from the playlist
#for video in playlist.video_urls:
#    print("'" + video + "' ,")