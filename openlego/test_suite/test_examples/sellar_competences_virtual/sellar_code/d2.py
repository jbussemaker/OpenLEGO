"""
This file represents the D2 discipline of the Sellar problem:

    y2 = sqrt(y1) + z1 + z2

Call using:
    python d2.py input.xml output.xml

The script is written for Python 2.7!

Copyright 2018, DLR, Jasper Bussemaker.
Licence: MIT
"""
import math
import argparse
from lxml import etree
from openlego.utils.xml_utils import xml_safe_create_element


def run(input_xml_file, output_xml_file):
    # Load input file
    tree = etree.parse(input_xml_file)
    root = tree.getroot()

    # Load input parameters for this discipline
    z1 = float(root.find('./variables/z1').text)
    z2 = float(root.find('./variables/z2').text)
    y1 = float(root.find('./analyses/y1').text)

    # "Run" the discipline calculations
    y2 = math.sqrt(y1) + z1 + z2

    # Write the output
    xml_safe_create_element(tree, '/dataSchema/analyses/y2', str(y2))

    tree.write(output_xml_file)


if __name__ == '__main__':
    # Define the command line arguments
    parser = argparse.ArgumentParser('Sellar D2')
    parser.add_argument('input_xml', help='The input XML file containing the Sellar central data schema')
    parser.add_argument('output_xml', help='The output XML file that will be written by this script')
    args = parser.parse_args()

    # Run the discipline
    run(args.input_xml, args.output_xml)
