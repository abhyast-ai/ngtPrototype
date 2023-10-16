import os
import xml.etree.ElementTree as ET


current_directory=os.getcwd()

# Directory containing Pascal VOC XML files
xml_directory=os.path.join(current_directory, "data", "custom_dataset","test")
# Directory to save YOLO format TXT files in a "labels" folder
labels_directory = './testlabels'

# Ensure the labels directory exists
os.makedirs(labels_directory, exist_ok=True)

# Iterate through XML files and convert to YOLO format
for xml_file in os.listdir(xml_directory):
    if xml_file.endswith(".xml"):
        xml_path = os.path.join(xml_directory, xml_file)
        txt_filename = os.path.splitext(xml_file)[0] + ".txt"
        txt_path = os.path.join(labels_directory, txt_filename)
        
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        with open(txt_path, 'w') as txt_file:
            for obj in root.findall('object'):
                class_name = obj.find('name').text
                bndbox = obj.find('bndbox')
                
                # Extract bounding box coordinates
                xmin = float(bndbox.find('xmin').text)
                ymin = float(bndbox.find('ymin').text)
                xmax = float(bndbox.find('xmax').text)
                ymax = float(bndbox.find('ymax').text)
                
                # Calculate YOLO format values
                width = xmax - xmin
                height = ymax - ymin
                x_center = (xmin + xmax) / 2
                y_center = (ymin + ymax) / 2
                
                # Write to YOLO format TXT file
                txt_file.write(f"{class_name} {x_center} {y_center} {width} {height}\n")

print("Conversion complete. YOLO format TXT files saved in the 'labels' folder.")
