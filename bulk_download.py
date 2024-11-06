import os
import pandas as pd
import requests
from urllib.parse import urlparse

# Path to the uploaded Excel file
excel_file_path = 'C:/Users/rushi/Downloads/leaving_certificicate.xlsx'

# Load the Excel file
df = pd.read_excel(excel_file_path)

# Create a download directory if it doesn't exist
download_dir = 'downloads'
os.makedirs(download_dir, exist_ok=True)

# Loop through each row to download and rename documents
for _, row in df.iterrows():
    candidate_name = row['Candidate_name']
    admission_doc_url = row['leaving_Certificate']
    
    # Parse the file extension from the URL
    path = urlparse(admission_doc_url).path
    file_extension = os.path.splitext(path)[-1]
    
    # Download the file
    response = requests.get(admission_doc_url)
    if response.status_code == 200:
        # Save the file with the original extension
        file_path = os.path.join(download_dir, f"{candidate_name}_LC{file_extension}")
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {candidate_name}'s document as {os.path.basename(file_path)}")
    else:
        print(f"Failed to download document for {candidate_name}")

print("Download completed.")
