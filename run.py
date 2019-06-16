from UserInterface import UserInterface
from WebCrawler import WebCrawler
from time import sleep

ui = UserInterface()

def main():

    wc = WebCrawler()
    wc.setDriverPath('chromedriver')
    wc.createDriver()

    searchTerm = 'irritable+bowel+disease'

    urlSequence = ('https://clinicaltrials.gov/ct2/results?cond=', searchTerm)
    url = ''.join(map(str, urlSequence))

    if wc.connectToURL(url, 'tab-body'):
        sleep(2)
        html = wc.getDriver().page_source
    else:
        print('Error connecting to URL')

    wc.killDriver()


    #ui.getDashboard('irritable bowel disease')

if __name__ == "__main__":
    main()