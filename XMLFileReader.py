#parses XML files
#author - steve

import xml.etree.ElementTree as et
import pandas as pd

def readXML(xmlFile, childName):
    # Takes in a file path and a string for referencing the elements in the XML.
    # Returns a pandas DataFrame
    tree = et.parse(xmlFile)
    root = tree.getroot()
    output = []
    for child in root.findall(childName):
        childInfo = {}
        for header in child:
            childInfo[header.tag] = header.text
        output.append(childInfo)
    return pd.DataFrame.from_dict(output)
