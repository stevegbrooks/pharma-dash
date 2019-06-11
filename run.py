import matplotlib.pyplot as plt
import pandas as pd
import XMLFileReader as xfr
import CTGov as ctgov

def main():
    searchResults = xfr.parseXML('SearchResults.xml', 'study')
    searchResults = pd.DataFrame.from_dict(searchResults)
    searchResults = ctgov.cleanData(searchResults)

    # study status by study type
    pd.set_option("display.max_columns", 12)
    print(pd.crosstab(searchResults['status'], searchResults['study_types']))

    # number of studies by year and status
    byYear = pd.crosstab(searchResults['start_year'], searchResults['study_types'])
    print(byYear)
    byYear.plot(xlim=[2000, 2019])
    plt.show()

if __name__ == "__main__":
    main()