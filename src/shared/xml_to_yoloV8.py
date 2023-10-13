import xml.etree.ElementTree as ET
import os
import glob

current_directory = os.getcwd()

data_dir = os.path.join(current_directory, 'data', 'custom_dataset')
model_dataset_dir = os.path.join(current_directory, 'data', 'model_dataset')
Dataset_names_path = os.path.join(model_dataset_dir, 'license_plate_names.txt')
Dataset_train = os.path.join(model_dataset_dir, 'license_plate_train.txt')
Dataset_test = os.path.join(model_dataset_dir, 'license_plate_test.txt')
is_subfolder = False

Dataset_names = []

def ParseXML(img_folder, file):
    for xml_file in glob.glob(img_folder + '/*.xml'):
        tree = ET.parse(open(xml_file))
        root = tree.getroot()
        image_name = root.find('filename').text
        img_path = os.path.join(img_folder, image_name)
        annotations = []

        for obj in root.iter('object'):
            cls = obj.find('name').text

            if cls not in Dataset_names:
                Dataset_names.append(cls)

            cls_id = Dataset_names.index(cls)
            xmlbox = obj.find('bndbox')

            # Convert the floating-point values to integers
            xmin = int(float(xmlbox.find('xmin').text))
            ymin = int(float(xmlbox.find('ymin').text))
            xmax = int(float(xmlbox.find('xmax').text))
            ymax = int(float(xmlbox.find('ymax').text))

            width = xmax - xmin
            height = ymax - ymin

            x_center = (xmin + width / 2)
            y_center = (ymin + height / 2)
            box_width = width
            box_height = height

            annotations.append(f"{cls_id} {x_center} {y_center} {box_width} {box_height}")

        if annotations:
            img_path += ' ' + ' '.join(annotations)
            print(img_path)
            file.write(img_path + '\n')


def run_XML_to_YOLOv8():
    os.makedirs(model_dataset_dir, exist_ok=True)  # Ensure the model_dataset directory exists
    for i, folder in enumerate(['train', 'test']):
        with open([Dataset_train, Dataset_test][i], "w") as file:
            img_path = os.path.join(data_dir, folder)
            if is_subfolder:
                for directory in os.listdir(img_path):
                    xml_path = os.path.join(img_path, directory)
                    ParseXML(xml_path, file)
            else:
                ParseXML(img_path, file)

    print("Dataset_names:", Dataset_names)
    with open(Dataset_names_path, "w") as file:
        for name in Dataset_names:
            file.write(str(name) + '\n')

run_XML_to_YOLOv8()
