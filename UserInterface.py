# Takes in requests from the user and returns desired output
# In this case, it will take in a search term, such as 'liver cancer',
# and return a dashboard based on the clinicaltrials.gov data

from CTGov import CTGov
import Display as disp

class UserInterface:

    def __init__(self):
        self.ctgov = CTGov()

    def getDashboard(self, searchTerm):
        searchResults = self.ctgov.getData(searchTerm)
        return disp.createDisplay(searchResults)

