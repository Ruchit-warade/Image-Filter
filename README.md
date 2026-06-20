# Image Filter Studio

A simple image editing project built using Python, NumPy, and Pillow.

I created this project to understand how image processing works at the pixel level without relying on high-level image editing libraries. The application allows users to load an image, apply different filters, and save the processed result.

## Features

* Adjust image brightness
* Change image contrast
* Convert images to grayscale
* Crop images from the center
* Remove individual RGB color channels
* Apply a basic blur effect
* View image information before processing
* Apply multiple filters one after another

## Installation

Clone the repository:

```bash
git clone https://github.com/Ruchit-warade/Image-Filter.git
cd Image-Filter
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Requirements

The project uses:

* NumPy
* Pillow
* tqdm

Python 3.8+ is recommended.

## How to Run

Run the script:

```bash
python image_filter.py
```

When prompted, enter the name of the image file you want to edit:

```text
Enter image filename: sample.jpg
```

After loading the image, choose one of the available filters from the menu.

## Available Filters

### Brightness

Increase the brightness of the image by adding a value to every pixel.

### Contrast

Adjust image contrast using a custom contrast factor.

### Grayscale

Convert a color image into grayscale using standard RGB weighting.

### Crop

Crop the image from the center by specifying the desired width and height.

### Remove Red Channel

Removes all red values from the image.

### Remove Green Channel

Removes all green values from the image.

### Remove Blue Channel

Removes all blue values from the image.

### Blur

Applies a simple 3×3 averaging blur filter.

## Example

```text
=======================================
|         IMAGE FILTER STUDIO         |
=======================================

Enter image filename: sample.jpg

Press 1: Brightness
Press 2: Contrast
Press 3: Grayscale
Press 4: Crop
Press 5: Remove Red Channel
Press 6: Remove Green Channel
Press 7: Remove Blue Channel
Press 8: Blur
```

After processing, the output image is automatically saved as:

```text
output.png
```

If you choose to apply more filters, the program uses the previously generated `output.png` as the new input image.

## Error Handling

The program handles:

* Missing image files
* Invalid image formats
* Incorrect menu choices
* Invalid contrast values
* Crop dimensions larger than the image size

## What I Learned

While building this project, I learned:

* How digital images are represented as arrays
* Basic image manipulation using NumPy
* Working with Pillow for image I/O
* Implementing common image filters manually
* Handling user input and exceptions in Python

## Future Improvements

Some features I plan to add in the future:

* Image rotation
* Sharpen filter
* Edge detection
* Gaussian blur
* Undo functionality
* GUI version using Tkinter

## Author

Ruchit Warade

GitHub: https://github.com/Ruchit-warade

Feel free to fork the project, suggest improvements, or open an issue if you find a bug.
