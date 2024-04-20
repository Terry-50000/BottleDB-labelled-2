import os

def replace_text_in_files(directory, old_text, new_text):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return

    # Loop through all the files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # Check if it's a file and not a directory
        if os.path.isfile(filepath):
            # Open the file and read contents
            with open(filepath, 'r', encoding='utf-8') as file:
                contents = file.read()

#Replace old text with new text
            contents = contents.replace(old_text, new_text)

#Write changes back to the file
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(contents)
            print(f"Replaced text in {filename}")

#Example usage
directory_path = 'D:\\Work\\yolo_augment\\dataset\\labels'
replace_text_in_files(directory_path, '0 ', '39 ')
