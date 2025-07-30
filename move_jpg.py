import os
import shutil

source = r"C:\Users\Windows 11\Desktop\source"
destination = r"C:\Users\Windows 11\Desktop\destination"

if not os.path.exists(destination):
    os.makedirs(destination)

jpg_files = [file for file in os.listdir(source) if file.lower().endswith(".jpg")]

if not jpg_files:
    print("No .jpg files found in the source folder.")
else:
    for file in jpg_files:
        source_path = os.path.join(source, file)
        destination_path = os.path.join(destination, file)
        shutil.move(source_path, destination_path)
        print(f"Moved: {file}")
    print("All .jpg files moved successfully!")
