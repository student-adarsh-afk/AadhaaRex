# modules 
import pytesseract
import re
import json
import cv2


# loading and reading the image using opencv
image_path = 'data/addhar.png'
image = cv2.imread(image_path)


# i am doing two passes with different preprocessing techniques to get better results
# First pass: convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Preprocess for first pass
gray = cv2.resize(gray_image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
gray = cv2.GaussianBlur(gray, (5,5), 0)

# reading both hindi and english 
text = pytesseract.image_to_string(gray,lang='eng+hin')

# first pass is not reading the name properly so i am doing second pass
# for getting the name of the person i am re reading the image with thresholding
_, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
for_name = pytesseract.image_to_string(binary_image,lang='eng+hin')

# Save the extracted text to a file 
with open('output/raw.txt', 'w') as text_file:
    text_file.write(text)
print("Text extraction complete. Check output/raw.txt for the result.")



# Function to extract relevant data
def extract_data(text):
    data = {
        "document_type": "Aadhaar Card",
        "name": None,
        "father_name": None,
        "dob": None,
        "gender": None,
        "aadhaar_number": None
    }

    # Normalize text
    text = re.sub(r'\s+', ' ', text)

    # Name (uppercase words, usually near top)
    name_match = re.search(r'\b([A-Z]{3,}(?:\s[A-Z]{3,})+)\b', for_name)
    if name_match:
        data["name"] = name_match.group(1)

    # Father name
    father_match = re.search(r'Father\s*:\s*([A-Za-z\s]+)', text, re.IGNORECASE)
    if father_match:
        data["father_name"] = father_match.group(1).strip()

    # DOB
    dob_match = re.search(r'\d{2}/\d{2}/\d{4}', text)
    if dob_match:
        data["dob"] = dob_match.group()

    # Gender
    if re.search(r'\bMale\b', text, re.IGNORECASE):
        data["gender"] = "Male"
    elif re.search(r'\bFemale\b', text, re.IGNORECASE):
        data["gender"] = "Female"

    # Aadhaar number (with or without spaces)
    aadhaar_match = re.search(r'\b\d{4}\s?\d{4}\s?\d{4}\b', text)
    if aadhaar_match:
        data["aadhaar_number"] = aadhaar_match.group().replace(" ", "")

    return data

# Extract data
extracted_data = extract_data(text)

# Convert to JSON
json_output = json.dumps(extracted_data, indent=4)

print(json_output)

# Save the JSON output to a file
with open('output/output.json', 'w') as json_file:
    json_file.write(json_output)
