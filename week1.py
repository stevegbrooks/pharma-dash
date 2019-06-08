#Week 1 assignment:
#
# 1. download the XML data from clinicaltrials.gov for the search term 'irritable bowel disease'
# 2. bring it into python and try to build a prototype descriptive stats dashboard

import xml.etree.ElementTree as ET
import pandas as pd

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

def cleanData_CT(searchResults):
    dateCols = ['completion_date', 'last_update_posted',
                'primary_completion_date', 'results_first_posted',
                'start_date', 'study_first_posted']
    searchResults[dateCols] = searchResults[dateCols].apply(pd.to_datetime)
    searchResults['start_year'] = searchResults['start_date'].apply(lambda x: x.year)
    searchResults['start_month'] = searchResults['start_date'].apply(lambda x: x.month)
    return searchResults

def main():

    searchResults = parseXML('SearchResults.xml', 'study')
    searchResults = pd.DataFrame.from_dict(searchResults)
    searchResults = cleanData_CT(searchResults)

    #study status by study type
    pd.set_option("display.max_columns", 12)
    print(pd.crosstab(searchResults['status'], searchResults['study_types']))

    #number of studies by year and status
    byYear = pd.crosstab(searchResults['start_year'], searchResults['study_types'])
    print(byYear)

    #graph it
    byYear.plot(xlim = [2000, 2019])

if __name__ == "__main__":
    # calling main function
    main()