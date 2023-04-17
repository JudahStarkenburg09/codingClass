import pytube
import moviepy.editor as mp
import os
import pygame

def downloadAndPlay():
    # Enter the YouTube video URL
    url = str(findFirstResult)

    # Create a PyTube object and extract the audio stream
    yt = pytube.YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()

    # Download the audio stream as a temporary file
    temp_file = stream.download()

    # Load the audio file with MoviePy and save it as a WAV file
    audio = mp.AudioFileClip(temp_file)
    audio.write_audiofile("audio.wav")
    pygame.init()
    pygame.mixer.music.load("audio.wav")
    pygame.mixer.music.play()
    input('stop press enter')

searched = input("What song would you like to play (Title and Author)? ")
query = searched
results = pytube.Search(query).results

if len(results) > 0:
    first_video_url = 'https://www.youtube.com' + results[0].watch_url
    findFirstResult = first_video_url.replace("watch?v=", "")
    downloadAndPlay()
else:
    print("No videos found for the given query.")
