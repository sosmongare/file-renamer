import os

directory = 'E:/myfolder/docs/Terry Documents'  # Change this to the path where your files are


name_to_append = " - Teresa Erukudi" # Define the name to append to the end of the file

# Loop through all the files in the directory
for filename in os.listdir(directory):
    # Check if the file is a PDF file
    if filename.endswith(".pdf"):
        # Get the current file path
        current_path = os.path.join(directory, filename)
        
        # Create the new file name by appending the name
        new_filename = filename.replace(".pdf", "") + name_to_append + ".pdf"
        new_path = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(current_path, new_path)

        print(f'Renamed: {filename} -> {new_filename}')
