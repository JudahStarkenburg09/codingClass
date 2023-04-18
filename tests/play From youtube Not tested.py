from pytube import YouTube
import subprocess
import time

def playFromYoutube(query):
    query = query.replace(' ', '+')
    url = f'https://www.youtube.com/results?search_query={query}'
    html = subprocess.check_output(f'curl "{url}"', shell=True).decode()
    video_id = html.split('watch?v=')[1].split('"')[0]

    # create the YouTube object and stream the audio
    yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')
    audio_stream = yt.streams.filter(only_audio=True).first()

    # play the audio stream
    audio_stream_url = audio_stream.url
    subprocess.Popen(f"mpv --no-video {audio_stream_url}", shell=True)

    # wait for the audio to finish playing
    while True:
        time.sleep(1)
        if subprocess.Popen.poll(subprocess.Popen(["pgrep", "mpv"])) is not None:
            break


playFromYoutube(query = input('song and author?" '))