import os
import pandas as pd
import requests

# Path to the uploaded Excel file
excel_file_path = 'C:/Users/rushi/Downloads/admission_letter_student_files_above_256kb.xlsx'

# Load the Excel file
df = pd.read_excel(excel_file_path)

# Create a download directory if it doesn't exist
download_dir = 'downloads'
os.makedirs(download_dir, exist_ok=True)

# Loop through each row to download and rename documents
for _, row in df.iterrows():
    candidate_name = row['Candidate_name']
    admission_doc_url = row['admission_letter_doc']
    
    # Assuming the URL is a direct link to download a file
    # Download file
    response = requests.get(admission_doc_url)
    if response.status_code == 200:
        # Save the file with Candidate_name as the filename
        file_path = os.path.join(download_dir, f"{candidate_name}_admission_letter.pdf")
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {candidate_name}'s document as {candidate_name}_admission_letter.pdf")
    else:
        print(f"Failed to download document for {candidate_name}")

print("Download completed.")
