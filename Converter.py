# Import dependencies
from pytube import YouTube
import os
import sys

# URL input
song = YouTube(str(input("What song would you like to Download: \n>> ")))

# Extract audio
audio = song.streams.filter(only_audio = True).first()

# Select the destination
#print("Select destination for song or leave blank for actual directory")
#destination = str(input(">> ")) or '.'
destination = r"C:\Users\Usuario\OneDrive\Escritorio\Musica"
# Download file
out_file = audio.download(output_path = destination)

# Save the file
base, ext =  os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)   

# Result of success 
print(song.title + " Has been successfully Downloaded.")