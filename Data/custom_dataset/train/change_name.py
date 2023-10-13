import os
import xml.etree.ElementTree as ET

# Specify the directory containing the XML files
xml_directory = "C:/Users/abhyasttripathi/workspace/git-abhyast/ngtPrototype/custom_dataset/train/annotations"

# Iterate through files in the directory
for filename in os.listdir(xml_directory):
    if filename.endswith(".xml"):
        # Create the full path to the XML file
        xml_file = os.path.join(xml_directory, filename)

        # Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Find and update the <name> element
        for object_elem in root.iter("object"):
            name_elem = object_elem.find("name")
            if name_elem is not None and name_elem.text == "licence":
                name_elem.text = "license-plate"

        # Save the modified XML file
        tree.write(xml_file)

print("XML files processed and modified.")
