import os
import subprocess

SUPPORTED_EXTENSIONS = [".jpg", ".jpeg", ".png"]

def import_photos(directory):
    # Get the list of files in the chosen directory
    files = os.listdir(directory)
    
    for file in files:
        # Check if the file is an image
        if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
            # Build the full path of the image file
            file_path = os.path.join(directory, file)
            
            # Use the 'osascript' command to run an AppleScript
            script = f'tell application "Photos" to import POSIX file "{file_path}"'
            subprocess.run(['osascript', '-e', script])
            
    print("Photos imported successfully!")

# Example usage
chosen_directory = "/path/to/your/chosen/directory"
import_photos(chosen_directory)
