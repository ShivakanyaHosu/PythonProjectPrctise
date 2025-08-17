import os

from dotenv import load_dotenv


class VWOloginPage:

    def __init__(self, email_org, password_org):
        self.email = email_org
        self.password = password_org

    def login_confirm(self):
        if self.email == "shivakanya@gmail.com" and self.password == "Pass123":
            print("Allowed, Login Sucess")
        else:
            print("Login Failed")


load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
# email = input("Enter the email \n")
# password = input("Enter the password \n")

VWO_obj = VWOloginPage(email, password)
VWO_obj.login_confirm()
