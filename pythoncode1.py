import xml.etree.ElementTree as ET
import csv
import logging
import boto3

# To Parse the XML file
tree = ET.parse('Assesment.xml')
root = tree.getroot()

# Open a CSV file in write mode
with open('SteelEye.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Write the CSV header
    writer.writerow(['checksum', 'download_link', 'publication_date', 'id', 'published_instrument_file_id', '_root_', 'file_name', 'file_type', '_version_', 'timestamp'])

    # Loop through each 'doc' element in the XML file
    for doc in root.findall('.//doc'):
        # Extract the values from the XML elements
        checksum = doc.find('str[@name="checksum"]').text
        download_link = doc.find('str[@name="download_link"]').text
        publication_date = doc.find('date[@name="publication_date"]').text
        id = doc.find('str[@name="id"]').text
        published_instrument_file_id = doc.find('str[@name="published_instrument_file_id"]').text
        _root_ = doc.find('str[@name="_root_"]').text
        file_name = doc.find('str[@name="file_name"]').text
        file_type = doc.find('str[@name="file_type"]').text
        _version_ = doc.find('long[@name="_version_"]').text
        timestamp = doc.find('date[@name="timestamp"]').text

        # Write the values to the CSV file
        writer.writerow([checksum, download_link, publication_date, id, published_instrument_file_id, _root_, file_name, file_type, _version_, timestamp])
print("XML to CSV conversion complete. CSV file created as 'output.csv'.")

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'XML_Assesment'
    file_name = 'finaloutputcsv.csv'
    s3.upload_file(file_name, bucket_name, file_name)