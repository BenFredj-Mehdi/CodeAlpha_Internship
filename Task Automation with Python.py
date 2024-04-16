import os
import shutil

# Function to organize files into directories based on their extensions
def organize_files(directory):
    # Create a dictionary to map file extensions to directory names
    extensions = {
        'txt': 'TextFiles',
        'pdf': 'PDFFiles',
        'jpg': 'ImageFiles',
        'xlsx': 'ExcelFiles',
        # Add more extensions and corresponding directories as needed
    }

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        # Ignore directories
        if os.path.isdir(filename):
            continue

        # Get the file extension
        _, ext = os.path.splitext(filename)
        ext = ext[1:].lower()  # Remove the dot and convert to lowercase

        # Check if the extension is mapped in the dictionary
        if ext in extensions:
            # Create the directory if it doesn't exist
            dest_dir = os.path.join(directory, extensions[ext])
            os.makedirs(dest_dir, exist_ok=True)

            # Move the file to the corresponding directory
            shutil.move(os.path.join(directory, filename), dest_dir)
            print(f"Moved {filename} to {extensions[ext]} directory.")

# Example usage
if __name__ == "__main__":
    directory_to_organize = '/path/to/your/directory'
    organize_files(directory_to_organize)
