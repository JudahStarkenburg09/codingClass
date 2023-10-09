import subprocess

def install_modules():
    # List of modules you want to install
    modules_to_install = [
        "pydrive",
        "pygame",
        "winshell",
        "threading",
        "os",
        "time",
        "tkinter"
    ]

    for module in modules_to_install:
        try:
            # Run the 'pip install' command for each module
            subprocess.run(["pip", "install", module], check=True)
            print(f"Successfully installed {module}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {module}")

if __name__ == "__main__":
    install_modules()
