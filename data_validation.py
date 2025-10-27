import json

def validate_data(ocr_text, json_data):
    try:
        expected_data = json.loads(json_data)
        if not all(key in expected_data for key in ["name", "dob"]):
            print("Mismatch Found")
            return

        ocr_parts = ocr_text.strip().split()
        if len(ocr_parts) < 2:
            print("Mismatch Found")
            return

        ocr_name = " ".join(ocr_parts[:-1])
        ocr_dob = ocr_parts[-1]

        if (expected_data["name"].lower().strip() == ocr_name.lower().strip() and
            expected_data["dob"].strip() == ocr_dob.strip()):
            print("Document Verified")
        else:
            print("Mismatch Found")

    except Exception:
        print("Mismatch Found")

ocr_text = input().strip()
json_data = input().strip()

validate_data(ocr_text, json_data)



