ocr_text = """
Name: Ravi Kumar
Date of Birth: 1998-04-12
""".strip()

json_data = {
    "name": "Ravi Kumar",
    "dob": "1998-04-12"
}

def extract_ocr_data(ocr_text):
    lines = ocr_text.split("\n")
    name = lines[0].split(":", 1)[1].strip()
    dob = lines[1].split(":", 1)[1].strip()
    return {"name": name, "dob": dob}

def verify_document(ocr_text, json_data):
    extracted_data = extract_ocr_data(ocr_text)
    print("Extracted OCR Data:", extracted_data)
    print("Expected JSON Data:", json_data)
    if extracted_data == json_data:
        print("Document Verified")
    else:
        print("Mismatch Found")

if __name__ == "__main__":
    verify_document(ocr_text, json_data)


