import inspect
import logging

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("launchBrowser")
class BaseClass:

    def actionsmethod(self, type, locator):
        actions = ActionChains(self.driver)
        if type =="mousehover":
            actions.move_to_element(locator).perform()
        elif type == "click":
            actions.click(locator).perform()

    def explicitwait(self, text):
        ExplicitWait = WebDriverWait(self.driver, 5)
        ExplicitWait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT, text))

    def getlogreport(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('C:\pythonsel\Reports\logfile.log')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger