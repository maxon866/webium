from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

webelement_class = WebElement
driver_class = Firefox
implicit_timeout = 30
wait_timeout = 30

default_search_type = By.ID

try:
    from local_webium_settings import *  # noqa
except ImportError:
    pass
