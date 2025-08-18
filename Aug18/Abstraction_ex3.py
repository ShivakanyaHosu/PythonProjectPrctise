from abc import ABC, abstractmethod


class ExcelReader(ABC):
    @abstractmethod
    def readFromExcel(self):
        pass


class Browser(ExcelReader):

    @abstractmethod
    def start_browser(self):
        pass

    @abstractmethod
    def stop_browser(self):
        pass


class TC(Browser):
    def start_browser(self):
        print("starting the browser")

    def stop_browser(self):
        print("stopping the browser")

    def readFromExcel(self):
        print("read from excel is ready")

    def runTC(self):
        self.start_browser()
        self.readFromExcel()
        self.stop_browser()


tc = TC()
tc.runTC()
