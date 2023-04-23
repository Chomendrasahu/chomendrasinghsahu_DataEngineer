import xml.etree.ElementTree as ET
import csv

# Parse the XML file
tree = ET.parse('DLTINS_20210117_01of01.xml')
root = tree.getroot()

# Open a CSV file in write mode
with open('finaloutputcsv.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the CSV header
    csv_writer.writerow(['FinInstrmGnlAttrbts.Id', 'FinInstrmGnlAttrbts.FullNm',
                          'FinInstrmGnlAttrbts.ClssfctnTp', 'FinInstrmGnlAttrbts.CmmdtyDerivInd',
                          'FinInstrmGnlAttrbts.NtnlCcy', 'Issr'])
    
    # Extract data from XML and write to CSV
    for doc in root.findall('.//FinInstrmGnlAttrbts'):  # Update this path to match the structure of your XML
        id = doc.find('Id').text
        full_nm = doc.find('FullNm').text
        clssfctn_tp = doc.find('ClssfctnTp').text
        cmmdty_deriv_ind = doc.find('CmmdtyDerivInd').text
        ntnl_ccy = doc.find('NtnlCcy').text
        issr = doc.find('Issr').text
        
        # Write data to CSV
        csv_writer.writerow([id, full_nm, clssfctn_tp, cmmdty_deriv_ind, ntnl_ccy, issr])

print("XML to CSV conversion complete. CSV file created as 'finaloutputcsv.csv'.")
