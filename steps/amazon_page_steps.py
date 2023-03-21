from behave import *

@given("Home page: I am on amazon homepage")
def step_impl(context):
    context.home_page_object.navigate_to_homepage()

@when("Home page: I search for samsung from Electronics")
def step_impl(context):
    context.home_page_object.insert_search_value()
    context.home_page_object.choose_category()
    context.home_page_object.click_search_button()

@when("Results page: I am on results page")


@when("Results page: I select Cell Phones & Accessories")
def step_impl(context):
    context.home_page_object.select_filter_department()

@when("Results page: I click SAMSUNG on Featured Brands")
def step_impl(context):
    context.home_page_object.select_filter_brands()

@when("Results page: I select $200 & Above from Price")
def step_impl(context):
    context.home_page_object.select_filter_price()

@when("Results page: I select on Avg. Customer Review four stars & Up")
def step_impl(context):
    context.home_page_object.select_filter_review()

@when("Results page: I select condition New")
def step_impl(context):
    context.home_page_object.select_condition()

@when("Results page: I select Availability")
def step_impl(context):
    context.home_page_object.select_availability()

@then("Results page: I navigate back to homepage")
def step_impl(context):
    context.home_page_object.navigate_back_to_homepage()


