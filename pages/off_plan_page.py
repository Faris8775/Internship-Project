from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class OffPlanPage(Page):
    OFF_PLAN = (By.CSS_SELECTOR, '.menu-twobutton')
    OFF_PLAN_TEXT = (By.XPATH, "//*[text()='Off-plan']")
    OFF_PLAN_PROJECTS = (By.CSS_SELECTOR, 'div.cards-properties')
    PROJECT_NAME = (By.CSS_SELECTOR, 'div.project-name')
    PROJECT_IMG = (By.CSS_SELECTOR, 'div.project-image')

    # Click the Off-Plan button
    def click_off_plan_button(self):
        self.wait_and_click(*self.OFF_PLAN)

    def verify_off_plan_page(self):
        self.verify_text('Off-plan', *self.OFF_PLAN_TEXT)

    def verify_each_product_on_off_plan(self):
        # all_projects = self.driver.find_elements(*self.OFF_PLAN_PROJECTS)  # [WebEl1, WebEl2, WebEl3, WebEl4]
        # titles = self.driver.find_elements(*self.PROJECT_NAME)
        # print(titles)
        #
        # for title in titles:
        #     title_text = title.text
        #     assert title_text, 'Project title not shown'
        #     print(title)
        #     self.find_element(*self.PROJECT_IMG)

        element = self.find_element(*self.OFF_PLAN_PROJECTS)
        sleep(10)
        image_div = element.find_element(*self.PROJECT_IMG)
        image_style = image_div.get_attribute('style')
        assert 'background-image' in image_style and 'url(' in image_style, 'Element is missing a picture.'

        title_div = element.find_element(*self.PROJECT_NAME)
        assert title_div.text.strip() != '', 'Element is missing a title.'
