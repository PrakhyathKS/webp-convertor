from PIL import Image
import os

def convert_to_webp(input_folder, output_folder):
    # Get the list of files in the input folder
    files = os.listdir(input_folder)

    for file in files:
        # Construct the full path for the file
        file_path = os.path.join(input_folder, file)

        # Check if the file is an image (you can customize this check based on your file types)
        if os.path.isfile(file_path) and file.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                # Open the image using Pillow
                image = Image.open(file_path)

                # Construct the new file path with the .webp extension in the output folder
                new_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".webp")

                # Save the image in WebP format
                image.save(new_path, "WEBP")

                print(f'Converted: {file} to {os.path.basename(new_path)}')
            except Exception as e:
                print(f'Error converting {file}: {e}')

# Specify the input and output folder paths
input_folder_path = r"input_folder_path address"
output_folder_path = r"output_folder_path address"

# Call the function to convert files in the input folder to WebP format and store in the output folder
convert_to_webp(input_folder_path, output_folder_path)
