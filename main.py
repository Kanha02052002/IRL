import os
import re
import PyPDF2

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def get_pdf_list(directory):
    all_files = os.listdir(directory)
    pdf_files = [os.path.join(directory, file) for file in all_files if re.search(r'\.pdf$', file, re.IGNORECASE)]
    return pdf_files

def write_to_txt(processed_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in processed_data:
            file.write(line + '\n')

def process_data(directory, output_file):
    processed_data = []
    pdf_files = get_pdf_list(directory)
    for pdf in pdf_files:
        raw_data = read_pdf(pdf)
        cleaned_text = clean_text(raw_data)
        processed_data.append(cleaned_text)
        
    write_to_txt(processed_data, output_file)
    # print(f"Processed data has been written to {output_file}")

directory = 'data_pdf' 
output_file = 'cleaned_data.txt'

process_data(directory, output_file)


