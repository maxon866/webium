import os

from selenium import webdriver

class Chrome(webdriver.Chrome):

    def __init__(self, *ar, **kw):
        options = webdriver.ChromeOptions()
        options.binary_location = os.environ.get('CHROME_PATH', '')
        super().__init__(*ar, **kw, options=options)

driver_class = Chrome
