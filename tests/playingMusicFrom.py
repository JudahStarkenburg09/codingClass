import pytube
import os
import subprocess

def playFromYoutube(query):
    # Search for the first video on YouTube
    query = query.replace(' ', '+')
    url = f"https://www.youtube.com/results?search_query={query}"
    html = subprocess.check_output(f'youtube-dl --get-url "{url}"', shell=True).decode()
    video_url = html.splitlines()[0]

    # Create a PyTube object and extract the audio stream
    yt = pytube.YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()

    # Play the audio stream using ffplay
    os.system(f"ffplay -nodisp -autoexit -loglevel quiet -i \"{stream.url}\"")

query = input("What song would you like to play (Title and Author)? ")
playFromYoutube(query)
