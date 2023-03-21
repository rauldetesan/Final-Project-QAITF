from browser import Browser
from pages.amazon_page import Page

def before_all(context):
    context.browser = Browser()
    context.home_page_object = Page()

def after_all(context):
    context.browser.close()