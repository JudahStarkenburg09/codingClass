import pytube
import os

# Specify the name of the new folder
new_folder_name = "Outputs"

# Check if the folder already exists
if not os.path.exists(new_folder_name):
    # If it doesn't exist, create the new folder
    os.makedirs(new_folder_name)

# Change the working directory to the new folder
os.chdir(new_folder_name)

while True:
    def download_youtube_media(url, output_file):
        try:
            # Create a Pytube YouTube object
            yt = pytube.YouTube(url)

            # Check if the user requested an MP4 video
            if '.mp4' in output_file:
                video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                print("Please Wait, This May Take A While!")
                video_stream.download(output_path='.', filename=output_file)
            else:
                # Get the highest quality stream (audio only)
                audio_stream = yt.streams.filter(only_audio=True).first()

                if '.mp3' not in output_file:
                    if output_file == '':
                        output_file = "audio"
                    output_file += '.mp3'

                print("Please Wait, This May Take A While!")
                # Download the audio stream as an MP3 file in the current directory
                audio_stream.download(output_path='.', filename=output_file)

            print("Media downloaded as", output_file)
        except Exception as e:
            print("An error occurred:", str(e))

    if __name__ == "__main__":
        url = input("Enter the YouTube URL: ")
        output_file = input("Enter the output video/audio file name (e.g., 'audio.mp3', 'video.mp4'): ")
        download_youtube_media(url, output_file)
