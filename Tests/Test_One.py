from Tests.LoginLogoutTest import LoginLogoutTest


class Test_One(LoginLogoutTest):


    def test_caseOne(self, getcredentials):
        try:
            home_page = self.loginmethod(getcredentials)
        except Exception as e:
            print(e)



