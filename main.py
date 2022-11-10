import os
import shutil
import xml.etree.ElementTree as xmlET
from translater import latin2cyrillic, cyrillic2latin


def get_func(text, to_latin=False):
    if to_latin:
        return cyrillic2latin(text)
    return latin2cyrillic(text)


def extract_doc(file_name: str, folder_name):
    temp_file = "temp.zip"
    shutil.copy(file_name, temp_file)
    shutil.unpack_archive(temp_file, folder_name)
    os.remove(temp_file)


def replace_xml_doc(file_location):
    tree = xmlET.parse(file_location)
    root = tree.getroot()
    namespaces = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

    words = set()
    for e in root.findall('.//w:t', namespaces):
        words.add(e.text)

    with open(file_location, 'r', encoding='utf-8') as file:
        content = file.read()
        for word in words:
            content = content.replace(
                f'{word}</w:t>', f'{get_func(word)}</w:t>')
        with open(file_location, 'w', encoding='utf-8') as out_file:
            out_file.write(content)


def collect_doc(folder_name):
    temp_file = "temp.zip"
    word_file = "word.docx"
    shutil.make_archive("temp", "zip", folder_name)
    shutil.move(temp_file, word_file)


word_doc = "doc.docx"
folder = "temp_folder"
xml_file_location = f'{folder}/word/document.xml'

extract_doc(word_doc, folder)
replace_xml_doc(xml_file_location)
collect_doc(folder)
