import os

folder = "./output"

output_files = [f for f in os.listdir(folder) if f.endswith('.webp')]

for output_file in output_files:
    # Remove 'resized_' and '_0' from the filename, and lowercase the remaining name
    new_name = output_file.replace('resized_', '').replace('_0', '').lower()
    
    # Rename the file
    os.rename(os.path.join(folder, output_file), os.path.join(folder, new_name))

print("Finished renaming files.")
