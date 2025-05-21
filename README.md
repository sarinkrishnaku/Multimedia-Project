# Play MadLibs - Automated Worksheet Filler

## Overview
This project automates playing MadLibs by detecting blanks (underscore lines) in a worksheet image, prompting the user for words, and overlaying those words on the image to generate a completed MadLibs sheet.

## Requirements
- Python 3.x
- Libraries: `opencv-python`, `pillow`, `numpy`
- A MadLibs template image (`madlib_template.png`) containing blank lines represented by underscores or horizontal lines.
- A TrueType font file (`arial.ttf` or any `.ttf` font)

## Setup

1. Clone or download the project folder.
2. Place your MadLibs template image named `madlib_template.png` in the project folder.
3. Ensure you have the script to point to a system font path.
4. Install required Python packages:
   ```bash
   pip install opencv-python pillow numpy
