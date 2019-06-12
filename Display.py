# this handles dashboard generation

import matplotlib.pyplot as plt
import pandas as pd

def createDisplay(searchResults):
    # study status by study type
    pd.set_option("display.max_columns", 12)
    print(pd.crosstab(searchResults['status'], searchResults['study_types']))

    # number of studies by year and status
    byYear = pd.crosstab(searchResults['start_year'], searchResults['study_types'])
    print(byYear)
    byYear.plot(xlim=[2000, 2019])
    plt.show()
