# For cropping 256 x 144 images into 144x144 images with orientation center, left, right

import os
from PIL import Image

# Ensure 'output' directory exists, if not, create it
output_dir = './output-dota'
input_dir = "./input-dota"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get list of all image files in the current directory
image_files = [f for f in os.listdir(input_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Iterate over all image files
# for image_file in image_files:
#     # Open image file
#     with Image.open(os.path.join(input_dir, image_file)) as img:
#         # Get image size
#         width, height = img.size

#         # Check if the image is square
#         if width == height:
#             print(f'Processing file {image_file}...')
#             # Resize image
#             resized_img = img.crop((56, 0, 200, 144))

#             # Save resized image in 'output' directory in webp format
#             output_file = f'{output_dir}/resized_{os.path.splitext(image_file)[0]}.webp'
#             resized_img.save(output_file, 'webp')
#             print(f'Successfully resized and saved {image_file} as {output_file}')
#         else:
#             print(f'Skipping {image_file} as it is not a square image.')

def get_square_crop_dimension(img):
    width, height = img.size

    # Determine the size of the square (the smaller of width and height)
    square_size = min(width, height)

    # Calculate the left, top, right, and bottom coordinates for the crop
    left = (width - square_size) / 2
    top = (height - square_size) / 2
    right = (width + square_size) / 2
    bottom = (height + square_size) / 2

    crop_dimension = (left, top, right, bottom)

    return crop_dimension


# Iterate over all image files and print their name + dimensions
for image_file in image_files:
    # Open image file
    with Image.open(os.path.join(input_dir, image_file)) as img:
        # Get image size
        width, height = img.size

        # Print image file name and dimensions
        print(f'{image_file} ({width}x{height})')

left_heroes = ["alchemist", "keeper-of-the-light", "lina"]
right_heroes = ["anti-mage","death-prophet", "dragon-knight", "grimstroke", "lone-druid", "meepo"]

# custom? jakiro, ogre-magi
# Iterate over all image files and crop the image into squares
for image_file in image_files:
    # Open image file
    with Image.open(os.path.join(input_dir, image_file)) as img:
        # Get image size
        width, height = img.size

        print(f'Processing file {image_file}...')
        
        # Cropping image
        hero_name= image_file.split(".")[0]
        if hero_name in left_heroes:
            cropped_img = img.crop((0, 0, 144, 144))
        elif hero_name in right_heroes:
            cropped_img = img.crop((112, 0, 256, 144))
        else:
            # center crop
            cropped_img = img.crop(get_square_crop_dimension(img))

        # Save cropped image in 'output' directory in webp format
        output_file = f'{output_dir}/{os.path.splitext(image_file)[0]}_square.webp'
        cropped_img.save(output_file, 'webp')
        print(f'Successfully cropped and saved {image_file} as {output_file}')
