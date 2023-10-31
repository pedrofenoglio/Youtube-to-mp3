import os
import re
from playlist_converter import playlist  # Import the playlist from playlist_converter module

# Directory where you want to check for song files
directory_path = "D:\Folclore"

# List of YouTube song links (Assuming 'playlist' is defined in playlist_converter module)
youtube_links = playlist

# List to store YouTube links that need to be downloaded
links_to_download = []

# Function to extract the video ID from a YouTube link
def extract_video_id(link):
    match = re.search(r"(?i)\b(\w+\s?\w+)(?:\s+\w+)?\b", link)
    if match:
        return match.group(1)
    return None

# Iterate through the YouTube links
for link in youtube_links:
    video_id = extract_video_id(link)
    if video_id is None:
        print(f"Invalid YouTube link: {link}")
    else:
        song_found = False
        for filename in os.listdir(directory_path):
            if video_id in filename:
                song_found = True
                break
        if song_found:
            print(f"Song from YouTube link '{link}' is already in the directory.")
        else:
            links_to_download.append(link)

# Print the YouTube links to download
print("YouTube links to download:")
for link in links_to_download:
    print(link)

print(len(link))

