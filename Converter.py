from pytube import YouTube
import os
import subprocess
import song_regex
import playlist_converter

# Select the destination directory
destination = r"D:\Folclore"

# Decide between downloading a single song or multiple
amount = int(input("Select 1 for downloading a single song, 0 for various: "))

# Download logic
if amount == 1:
    # URL input
    url = str(input("What song would you like to Download: \n>> "))
    song = YouTube(url)

    # Download video
    video_stream = song.streams.filter(only_audio=True).first()
    video_stream.download(output_path=destination)

    # Get the downloaded video file path
    video_file_path = os.path.join(destination, song.title + f".{video_stream.subtype}")

    # Define the output audio file path (MP3)
    audio_file_path = os.path.join(destination, song.title + ".mp3")

    # Convert the video to audio (MP3) using FFmpeg
    subprocess.run(['ffmpeg', '-i', video_file_path, audio_file_path])

    # Remove the original video file
    os.remove(video_file_path)

    # Result of success
    print(f"{song.title} has been successfully downloaded as an MP3 file. The location is: {destination}")

elif amount == 0:
    ammount = int(input("Would you want to download a Youtube Playlist? Select 1 if so: "))
    if ammount == 1:
        songs = playlist_converter.playlist
        # Download and convert each song to audio (MP3)
        for song_url in songs:
            song = YouTube(song_url)
            video_stream = song.streams.filter(only_audio=True).first()
            video_stream.download(output_path=destination)
            video_file_path = os.path.join(destination, song.title + f".{video_stream.subtype}")
            audio_file_path = os.path.join(destination, song.title + ".mp3")
            subprocess.run(['ffmpeg', '-i', video_file_path, audio_file_path])
            os.remove(video_file_path)
            print(f"{song.title} has been successfully downloaded and saved as an MP3 file in {destination}\n")



    else:
        # Input: Enter song URLs
        print("Enter song URLs, when done write 'done'")
        songs = []
        while True:
            song_url = input("Enter a song URL (or 'done' to finish): ")
            if song_url.lower() == 'done':
                break
            songs.append(song_url)

        # Download and convert each song to audio (MP3)
        for song_url in songs:
            song = YouTube(song_url)
            video_stream = song.streams.filter(only_audio=True).first()
            video_stream.download(output_path=destination)
            video_file_path = os.path.join(destination, song.title + f".{video_stream.subtype}")
            audio_file_path = os.path.join(destination, song.title + ".mp3")
            subprocess.run(['ffmpeg', '-i', video_file_path, audio_file_path])
            os.remove(video_file_path)
            print(f"{song.title} has been successfully downloaded and saved as an MP3 file in {destination}\n")





    

    

    




