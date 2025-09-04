from browserpackage.OpenBrowser import open_browser
from browserpackage.CloseBrowser import close_browser


# open_browser()
# close_browser()

class TestCase:

    def Run_testcase(self):
        open_browser()
        close_browser()


obj = TestCase()
obj.Run_testcase()
