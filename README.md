# Python WebP Converter

A simple command-line tool to convert images (from a local file or a URL) into the WebP format with customizable quality.

## Overview

This project provides a lightweight Python script that converts images to the [WebP](https://developers.google.com/speed/webp) format. It supports both local image files and images downloaded from a URL. Converted images are saved in the output folder (default: `converted-images`).

## Features

- Dual Input Support: Convert images from a local file or directly from an online URL.
- Automatic Folder Creation: The output folder is automatically created if it doesn't exist.
- Quality Adjustment: Set the conversion quality (default is 80).
- Interactive Mode: Convert multiple images in one session without restarting the program.
- Error Handling: The script catches and displays errors during image download or conversion.

## Requirements

- Python 3.x
- Pillow (for image processing) - https://python-pillow.org/
- Requests (for downloading images) - https://docs.python-requests.org/en/latest/

## Installation

1. Clone the repository (if applicable):
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. Install the required libraries:
   pip install requests pillow

## Usage

You can run the script in two ways:

### Using a Command-Line Argument

Provide the image URL or local file path directly when running the script:
   python your_script_name.py <image_url_or_local_path>
Replace `<image_url_or_local_path>` with the URL or the path to your image.

### Interactive Mode

If no command-line argument is provided, the script will prompt you to enter the image URL or file path:
   python your_script_name.py
Follow the on-screen instructions to convert your image. After conversion, the resulting WebP file will be saved in the `converted-images` folder.

## Code Overview

- convert_to_webp(input_path, output_folder, quality=80):
  This function checks if the input is a URL or a local file. It then downloads (if needed), converts the image to WebP format, and saves it in the specified output folder.

- Interactive Loop:
  The script runs in a loop, allowing you to convert multiple images consecutively. It will ask if you want to convert another image after each conversion.

## Troubleshooting

- Invalid URL or Path: Ensure that the image URL or local file path is correct.
- Internet Connection: When using a URL, make sure your internet connection is stable.
- Library Installation: If you encounter errors related to missing libraries, double-check that you have installed both requests and pillow using pip.

## License

This project is open-source and available under the MIT License. (See LICENSE file)

## Acknowledgments

- Pillow Documentation: https://pillow.readthedocs.io/
- Requests Documentation: https://docs.python-requests.org/en/latest/
