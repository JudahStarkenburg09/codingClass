import subprocess

# Replace 'your_app_executable.exe' with the path to the executable of the app you want to run
app_to_run = 'your_app_executable.exe'

# Start the app with Python
subprocess.Popen([app_to_run], shell=True)
