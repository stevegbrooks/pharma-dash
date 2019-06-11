#This module retrieves and cleans data from the clinicaltrials.gov website
#author - steve

import pandas as pd

def getData(webDriver):
    #TODO implement
    pass

def cleanData(searchResults):
    dateCols = ['completion_date', 'last_update_posted',
                'primary_completion_date', 'results_first_posted',
                'start_date', 'study_first_posted']
    searchResults[dateCols] = searchResults[dateCols].apply(pd.to_datetime)
    searchResults['start_year'] = searchResults['start_date'].apply(lambda x: x.year)
    searchResults['start_month'] = searchResults['start_date'].apply(lambda x: x.month)
    return searchResults