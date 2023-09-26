import os
import shutil
import ctypes
import win32con
import win32api
import win32gui
import win32ui

def setIconForExe(exe_path, icon_path):
    """
    Set the icon for an exe file.

    :param exe_path: The path to the exe file.
    :param icon_path: The path to the icon file.
    """
    # Ensure both files exist
    if not os.path.exists(exe_path) or not os.path.exists(icon_path):
        print("Exe file or icon file does not exist.")
        return

    # Get the handle to the exe file
    exe_handle = win32ui.CreateFileIconExtractor(exe_path)

    # Extract the icon from the exe file
    icon_index = 0
    large, small = exe_handle.GetIcon(icon_index)

    # Save the icon as a .ico file
    icon_temp_path = os.path.join(os.path.dirname(exe_path), "temp.ico")
    small.SaveIcon(icon_temp_path)

    # Replace the icon in the exe file
    win32api.BeginUpdateResource(exe_path, False)
    win32api.UpdateResource(exe_path, win32con.RT_ICON, 1, win32con.LANG_NEUTRAL, open(icon_temp_path, "rb").read())
    win32api.EndUpdateResource(exe_path, False)

    # Clean up the temporary icon file
    os.remove(icon_temp_path)

# Example usage:
exe_destination_folder = os.path.join(os.getenv('LOCALAPPDATA'), 'Car Highway')
image_destination_folder = os.path.join(exe_destination_folder, 'images')
exe_file_path = os.path.join(exe_destination_folder, 'Car Highway.exe')
icon_file_path = os.path.join(image_destination_folder, 'CarHighwayLogo.ico')

setIconForExe(exe_file_path, icon_file_path)
