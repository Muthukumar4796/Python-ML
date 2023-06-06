# import PyPDF2
# import csv
#
# # Open the PDF file in read-binary mode
# pdf_file = open('1.2.826.1.3680043.9.5282.150415.2352.16502352212057.pdf', 'rb')
#
# pdf_reader = PyPDF2.PdfReader(pdf_file)
#
# num_pages = len(pdf_reader.pages)
#
# # Specify the CSV file path
# csv_file_path = 'output2.csv'
#
# # Write the extracted text to the CSV file
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Page Number', 'Text'])
#
#     for page_number in range(num_pages):
#         page = pdf_reader.pages[page_number]
#         page_text = page.extract_text()
#         writer.writerow([page_number + 1, page_text])
#
# print("Extraction completed. The text has been saved to", csv_file_path)

# Importing Required Modules
# from rembg import remove
# import os
#
# # Store path of the input image
# input_path = r'C:\Users\Asus\pythonProjectNLP\image(2).jpg'
#
# # Process the image and remove the background
# with open(input_path, 'rb') as img_file:
#     img_data = img_file.read()
#     output_data = remove(img_data)
#
# # Create the output file path for the cropped image
# output_filename = 'cropped_image2.jpg'
# output_path = os.path.join(os.path.dirname(input_path), output_filename)
#
# # Save the output image as the cropped image
# with open(output_path, 'wb') as output_file:
#     output_file.write(output_data)
#
# # Print a message to indicate successful background removal and save location
# print("Background removed successfully.")
# print("Cropped image saved at:", output_path)

# import os
# import requests
# from bs4 import BeautifulSoup
# from pdfminer.high_level import extract_text
#
# def extract_text_from_pdf(pdf_path):
#     return extract_text(pdf_path)
#
# def preprocess_text(text):
#     # Perform any necessary preprocessing steps
#     # e.g., removing unwanted characters or formatting
#
#     return text
#
# def identify_medical_terms(text):
#     # Use NER or other techniques to identify medical terms in the text
#     # and return a list of identified medical terms
#
#     medical_terms = []  # Replace with the actual implementation
#
#     return medical_terms
#
# def scrape_medical_dictionary(term):
#     url = "https://medical-dictionary.thefreedictionary.com/{}".format(term)
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     definition = soup.find(class_="ds-single")
#     if definition is not None:
#         return definition.get_text()
#     else:
#         return None
# print(scrape_medical_dictionary(term))
#
# def replace_medical_terms_with_definitions(text, medical_terms):
#     for term in medical_terms:
#         definition = scrape_medical_dictionary(term)
#         if definition is not None:
#             text = text.replace(term, definition)
#
#     return text
#
# def postprocess_text(text):
#     # Perform any necessary post-processing steps
#     # e.g., formatting or cleaning up the text
#
#     return text
#
# def convert_radiology_report(pdf_path, output_path):
#     # Step 1: Extract text from PDF
#     text = extract_text_from_pdf(pdf_path)
#
#     # Step 2: Preprocess text
#     text = preprocess_text(text)
#
#     # Step 3: Identify medical terms
#     medical_terms = identify_medical_terms(text)
#
#     # Step 4: Replace medical terms with definitions
#     text = replace_medical_terms_with_definitions(text, medical_terms)
#
#     # Step 5: Post-process text
#     text = postprocess_text(text)
#
#     # Save the translated radiology report to a file
#     with open(output_path, 'w', encoding='utf-8') as file:
#         file.write(text)
#
# # Example usage
# pdf_path = r"C:\Users\Asus\pythonProjectNLP\1.2.826.1.3680043.9.5282.150415.3080.16403080212057.pdf"
# # output_path = r"C:\Users\Asus\pythonProjectNLP\translated_report3.txt"
# convert_radiology_report(pdf_path, output_path)


import PyPDF2

def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Provide the path to your radiology report PDF file
pdf_file_path = "1.2.826.1.3680043.9.5282.150415.3080.16403080212057.pdf"

# Extract text from the PDF
report_text = extract_text_from_pdf(pdf_file_path)

import re
import requests

def replace_terms_with_definitions(text):
    # Identify technical terms using regular expressions
    technical_terms = re.findall(r"\b[A-Z]{2,}\b", text)  # Adjust the regex pattern as per your requirements

    for term in technical_terms:
        # Query UMLS API to retrieve the definition of the term
        url = f"https://uts-ws.nlm.nih.gov/rest/content/current/CUI/{term}"
        headers = {"Content-Type": "application/json"}
        params = {"ticket": "c886daef-d208-44d7-9ef9-03ec4d0604c0"}  # Replace with your UMLS API key
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            json_data = response.json()
            definition = json_data["result"]["name"]
            text = text.replace(term, definition)

    return text

# Replace technical terms with definitions
processed_text = replace_terms_with_definitions(report_text)

def save_text_as_pdf(text, output_file_path):
    with open(output_file_path, "w") as file:
        file.write(text)

# Provide the path to save the processed PDF file
output_pdf_path = r"C:\Users\Asus\pythonProjectNLP\output.pdf"

# Save the processed text as a PDF
save_text_as_pdf(processed_text, output_pdf_path)


