from selenium.webdriver.common.by import By

from pages.base_page import Base_page
from selenium.webdriver.support.select import Select

class Page(Base_page):
    SEARCH_TEXTBOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    SEARCH_CATEGORIES = (By.ID, "searchDropdownBox")
    FILTER_DEPARTMENT = (By.ID, "n/2811119011")
    FILTER_BRANDS = (By.ID, "p_89/SAMSUNG")
    FILTER_PRICE = (By.ID, "p_36/1253507011")
    FILTER_REVIEW = (By.ID, "p_72/1248879011")
    SELECT_CONDITION = (By.ID, "p_n_condition-type/2224371011")
    SELECT_AVAILABILITY = (By.ID, "p_n_availability/2661601011")

    def navigate_to_homepage(self):
        self.chrome.get("https://www.amazon.com/ref=nav_logo")

    def insert_search_value(self):
        self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys("samsung")

    def choose_category(self):
        category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORIES))
        category_dropdown.select_by_visible_text("Electronics")

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def select_filter_department(self):
        self.wait_and_click_element(*self.FILTER_DEPARTMENT)

    def select_filter_brands(self):
        self.wait_and_click_element(*self.FILTER_BRANDS)

    def select_filter_price(self):
        self.wait_and_click_element(*self.FILTER_PRICE)

    def select_filter_review(self):
        self.wait_and_click_element(*self.FILTER_REVIEW)

    def select_condition(self):
        self.wait_and_click_element(*self.SELECT_CONDITION)

    def select_availability(self):
        self.wait_and_click_element(*self.SELECT_AVAILABILITY)

    def navigate_back_to_homepage(self):
        self.chrome.get("https://www.amazon.com/ref=nav_logo")