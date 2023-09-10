import os
import subprocess
import sys

SUPPORTED_EXTENSIONS = [".jpg", ".jpeg", ".png"]

def import_photos(directory):
    # Get the list of files in the chosen directory
    files = os.listdir(directory)
    
    for file in files:
        # Check if the file is an image
        if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
            # Build the full path of the image file
            file_path = os.path.join(directory, file)
            
            # Print the name of the picture being imported
            print(f"Importing: {file}")
            
            # Use the 'osascript' command to run an AppleScript
            script = f'tell application "Photos"\nset importResult to import POSIX file "{file_path}" with skip check duplicates\nif importResult is not 0 then\nlog "Skipping import of duplicate file: {file}"\nend if\nend tell'
            subprocess.run(['osascript', '-e', script])
            
    print("Photos imported successfully!")

# Check if the directory argument is provided
if len(sys.argv) < 2:
    print("Please provide the directory path as a command line argument.")
    print("Usage: python import_photos.py /path/to/your/chosen/directory")
    sys.exit(1)

# Get the directory path from the command line argument
chosen_directory = sys.argv[1]

# Call the function with the provided directory path
import_photos(chosen_directory)
