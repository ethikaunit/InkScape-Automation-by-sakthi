import csv
import xml.etree.ElementTree as ET
import subprocess
import os

datasheet = 'data.csv'
output = '/temp'

getlist = []
value = 0

# Read data from CSV file
with open(datasheet, 'r') as data:
    for line in csv.reader(data, delimiter=','):
        getlist.append(line)

for names in getlist:
    replacements = {
        'VAR_name': 'value0',
        'VAR_cls': 'value1',
        'VAR_fname': 'value2', 
        'VAR_address': 'value3',
        'VAR_blood': 'value4',
        'VAR_dob': 'value5',
        'VAR_ph': 'value6',
        'VAR_Filename': 'value7'
        
       

    }
    replacements['VAR_name'] = names[0]
    replacements['VAR_cls'] = names[1]
    replacements['VAR_fname'] = names[2]
    replacements['VAR_address'] = names[3]
    replacements['VAR_blood'] = names[4]
    replacements['VAR_dob'] = names[5]
    replacements['VAR_ph'] = names[6]
    replacements['VAR_Filename'] = names[7]
    filename = names[7]
    
    # Parse SVG file
    tree = ET.parse('temp.svg')
    root = tree.getroot()
    
    # Iterate over 'tspan' elements in the SVG
    for tspan_elem in root.iter('{http://www.w3.org/2000/svg}tspan'):
        text = tspan_elem.text
        if text in replacements:
            tspan_elem.text = replacements[text]
            tspan_elem.text.replace(', ', ',\n')
        #naming = input(f"Give a name for svg :")
        tree.write(f".{output}//{filename}.svg", encoding='utf-8', xml_declaration=True)

    cmdl = 'inkscape ./temp/{0}.svg --export-type=png --export-dpi=300 --export-filename=./temp/exported/{1}.png'.format(filename,filename)
    cmd = cmdl
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print('{0} card completed'.format(value))
    print(replacements['VAR_Filename'])
    value = value + 1
