import time

import pytest

from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class LoginLogoutTest(BaseClass):
    try:
        def loginmethod(self, getcredentials):
            log = self.getlogreport()
            home_page = HomePage(self.driver)
            login_page = LoginPage(self.driver)
            login_page.findusernameBttn().send_keys(getcredentials["username"])
            login_page.findpasswordBttn().send_keys(getcredentials["password"])
            login_page.findloginBttn().click()
            log.info("Successfully logged into Flipkart application")
            time.sleep(5)
            return home_page
    except Exception as e:
        print(e)

    #def logoutmethod(self):
        #home_page = HomePage(self.driver)
        #self.actionsmethod("mousehover", home_page.findnavigatetousermenu())
        #home_page.findlogoutBttn().click()

    @pytest.fixture(params=HomePageData.login)
    def getcredentials(self, request):
        return request.param

