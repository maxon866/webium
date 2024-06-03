import webium.settings
from webium.jquery import JQuery


class Clickable(webium.settings.webelement_class):

    def click(self, jquery=False):
        """
        Click by WebElement, if not, JQuery click
        """
        if jquery:
            e = JQuery(self)
            e.click()
        else:
            super(Clickable, self).click()
