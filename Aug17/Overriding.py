class Oldbrowser:
    def start_browser(self):
        print("start browser")

    def stop_browser(self):
        print("stop browser")


class new_chrome_browser(Oldbrowser):
    def start_browser(self):
        super().start_browser()  # Parent start browser also
        print("better chrome browser can start .....")


obj_ref = new_chrome_browser()
obj_ref.start_browser()
obj_ref.stop_browser()
