#parses XML files
#author - steve

import xml.etree.ElementTree as ET

def parseXML(xmlFile, childName):
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    output = []
    for child in root.findall(childName):
        childInfo = {}
        for header in child:
            childInfo[header.tag] = header.text
        output.append(childInfo)
    return output