from selenium.webdriver.common.by import By

from pages.base_page import Page



class MainPage(Page):

    SIGNIN = (By.CSS_SELECTOR, '.sing-in-text')
    EMAIL = (By.CSS_SELECTOR, '#email-2')
    PASSWORD = (By.CSS_SELECTOR, '#field')
    LOGIN = (By.CSS_SELECTOR, '.login-button.w-button')



    # Open the Reelly website
    def open(self):
        self.open_url('https://soft.reelly.io/sign-up')

    # Click the Sign In
    def signin(self):
        self.click(*self.SIGNIN)

    # Enter Email and Password into input fields and click the Continue button
    def login(self):
        self.input_text('faruka16@gmail.com', *self.EMAIL)
        self.input_text('sLa6QJJfid!HPrEB', *self.PASSWORD)
        self.click(*self.LOGIN)







