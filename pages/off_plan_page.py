from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class OffPlanPage(Page):
    OFF_PLAN = (By.CSS_SELECTOR, '.menu-twobutton')
    # OFF_PLAN_TEXT = (By.XPATH, "//*[text()='Off-plan']")
    OFF_PLAN_PROJECTS = (By.CSS_SELECTOR, 'div.cards-properties')
    PROJECT_NAME = (By.CSS_SELECTOR, 'div.project-name')
    PROJECT_IMG = (By.CSS_SELECTOR, 'div.project-image')
    NEXT_PAGE = (By.CSS_SELECTOR, '.pagination__button.w-inline-block')

    # Click the Off-Plan button
    def click_off_plan_button(self):
        self.wait_and_click(*self.OFF_PLAN)

    def verify_off_plan_page(self):
        # self.verify_text('Off-plan', *self.OFF_PLAN_TEXT)
        self.verify_url('https://soft.reelly.io/')

    def verify_each_product_on_off_plan(self):

        element = self.find_element(*self.OFF_PLAN_PROJECTS)
        sleep(8)

        for page_num in range(1,52):
            sleep(6)
            image_div = element.find_element(*self.PROJECT_IMG)
            image_style = image_div.get_attribute('style')
            assert 'background-image' in image_style and 'url(' in image_style, 'Element is missing a picture.'

            title_div = element.find_element(*self.PROJECT_NAME)
            assert title_div.text.strip() != '', 'Element is missing a title.'
            self.click(*self.NEXT_PAGE)



