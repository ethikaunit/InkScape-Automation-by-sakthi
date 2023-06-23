import csv
import xml.etree.ElementTree as ET

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
        'VAR_dob': 'value2',
        'VAR_fname': 'value3',
        'VAR_address': 'value4',
        'VAR_ph': 'value5'

    }
    replacements['VAR_name'] = names[0]
    replacements['VAR_cls'] = names[1]
    replacements['VAR_dob'] = names[2]
    replacements['VAR_fname'] = names[3]
    replacements['VAR_address'] = names[4]
    replacements['VAR_ph'] = names[5]
    
    # Parse SVG file
    tree = ET.parse('template.svg')
    root = tree.getroot()
    
    # Iterate over 'tspan' elements in the SVG
    for tspan_elem in root.iter('{http://www.w3.org/2000/svg}tspan'):
        text = tspan_elem.text
        if text in replacements:
            tspan_elem.text = replacements[text]
            tspan_elem.text.replace(', ', ',\n')
        
        # Save modified SVG as a new file
        tree.write(f".{output}//file{value}.svg", encoding='utf-8', xml_declaration=True)
    
    print('{0} card completed'.format(value))
    value = value + 1
