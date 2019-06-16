#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 23:46:12 2018

@author: sgb
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebCrawler:
    
    class __WebCrawler:
        
        def __init__(self):
            pass
        
        def setDriverPath(self, driverPath):
            self.driverPath = driverPath
    
        def createDriver(self):
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            self.driver = webdriver.Chrome(
                    executable_path = self.driverPath, 
                    chrome_options=options
                    )
        
        def connectToURL(self, url, elementID):
#            self.driver.get_screenshot_as_file('beforeTry.png')
            connectionAttempts = 0
            while connectionAttempts < 3:
                try:
                    self.driver.get(url)
#                    self.driver.get_screenshot_as_file('afterTry.png')
                    WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, elementID))
                    )
                    return True
                except Exception as ex:
                    connectionAttempts += 1
                    print(f'Error connecting to {url}')
                    print(f'Attempt #{connectionAttempts}')
            return False

        def getDriver(self):
            return self.driver

        def killDriver(self):
            self.driver.quit()
    
    instance = None
    
    def __init__(self):
        if not WebCrawler.instance:
            WebCrawler.instance = WebCrawler.__WebCrawler()
    
    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    
    

