# Systemize Data Using OCR

![Project Banner Placeholder](data/banner.png)

A compact OCR pipeline for extracting text from identity card images (currently only aadhar). This repository demonstrates reading images, preprocessing them for robust OCR, and saving extracted text into a json format .

---

**Quick Links**
- **Code:** `main.py`
- **Dependencies:** `requirements.txt`
- **Sample data:** `data/`
- **Output:** `output/` (contains `output.txt` and debug images)

---

**Features**
- Read images of varying types (RGB, RGBA)
- Adaptive preprocessing (Otsu / adaptive thresholding)
- Resizing that preserves aspect ratio
- Save debug image used for OCR
- Write recognized text to `output/raw.txt`

---

**Requirements**
- Python 3.10+ (recommended)
- Tesseract OCR engine (system dependency)
- Python packages listed in `requirements.txt`


**Install Tesseract (macOS)**
```bash
# Using Homebrew
brew install tesseract
```

On Linux (Ubuntu):
```bash
sudo apt update
sudo apt install -y tesseract-ocr libtesseract-dev
```

On Windows: download the installer from the Tesseract project and add it to your PATH.

---

**Python dependencies**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, typical packages used by this project are:
```
pytesseract
opencv-python
pillow
```

---

**Installation & Run**

1. Clone the repository.
2. Install system dependency: Tesseract (see above).
3. Create and activate a virtual environment.
4. Install Python packages: `pip install -r requirements.txt`.
5. Place images under the `data/` folder (example: `data/addhar.png`).
6. Run:

```bash
python3 main.py
```

raw Output will be written to `output/raw.txt` and then after preprocessing the result will be in json format stored  in `output/output.json`

---

**Project Logic (Overview)**

This project follows a simple, robust pipeline to maximize OCR accuracy across varied input images:



1. First, we load the Aadhaar card image using OpenCV. This gives us the picture we want to read.
2. Preprocess the image (First Pass)
3. We convert the image to grayscale to make it simpler for the OCR to read.
4. Then we resize it to make it bigger, and apply a blur to reduce noise.
5. After this, we use Tesseract OCR to read both English and Hindi text from the image.
6. Preprocess the image (Second Pass for Name)
Sometimes the name doesn’t come out correctly in the first pass.
So, we try a different method called thresholding to make the text stand out more.
7. Then we read the name again using Tesseract.
8. Save raw text
9. Whatever text Tesseract gives us, we save it into a file called raw.txt so we can check it if needed.
10. Extract relevant information
We go through the raw text and look for specific pieces of info:
Name → Usually in uppercase, near the top of the card.
Father’s Name → Looks for text after the word “Father”.
Date of Birth → Looks for something like DD/MM/YYYY.
Gender → Checks for “Male” or “Female”.
Aadhaar Number → Looks for 12-digit number, sometimes written with spaces.
11. Convert to JSON
We organize all the extracted data into a clean JSON format for easy use in apps or databases.
12. Save JSON
Finally, we save the extracted JSON into a file called output.json.

---


**How I Can Improve This Project with NLP / LLM**

So right now, my code reads the Aadhaar card using OCR, does some preprocessing, and then I use regex to pick out the name, father’s name, DOB, gender, and Aadhaar number. It works, but it’s not perfect. Here’s how I can make it smarter with NLP or LLM:
1. Fix OCR Mistakes Automatically
2. Better Name and Father Name Extraction
   Right now I look for uppercase words or text after “Father: …”. An LLM can actually understand the context, so even if the layout changes or the text isn’t perfect, it can still pick the right names
3. Validate DOB and Aadhaar Number
   I just search for the date or 12-digit number right now. An LLM can check if the DOB makes sense or if the Aadhaar number is valid, reducing errors.
4. Handle Mixed Languages
    I use eng+hin, but an LLM can read multiple languages better and handle cards where text is mixed or partially unclear.



**assumptions**

1. Clear Image Input
The Aadhaar card image should be clear and not blurry. OCR works best on high-quality images.
2. Standard Aadhaar Layout
The card follows the typical Aadhaar format (name at top, DOB somewhere below, Aadhaar number at bottom, etc.).
3. Language Support
The text on the card is in English or Hindi. Other languages may not be recognized correctly.
4. Readable Text Size
Text is not too small or too faint. Very small fonts or extreme angles may cause wrong readings.
5. Single Person Card
The system assumes one Aadhaar card per image. Multiple cards in one image may not be processed correctly.
6. 12-Digit Aadhaar Number
The Aadhaar number is exactly 12 digits, sometimes with spaces. OCR may misread if digits are smudged.
7. No Handwritten Modifications
Any handwritten edits on the card (e.g., crossed out names) might not be read correctly.

---



**Contributing**

Contributions are welcome. Please fork the repo, make changes on a branch, and open a pull request. Add tests or sample images demonstrating fixes when possible.

---

*README generated and includes placeholders for an image and further explanation.*
