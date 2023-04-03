from behave import *


@given("Home page: I am on amazon homepage")
def step_impl(context):
    context.home_page_object.navigate_to_homepage()


@when('Home page: I search for "{product_name}" from "{category_name}"')
def step_impl(context, product_name, category_name):
    context.home_page_object.insert_search_value(product_name)
    context.home_page_object.choose_category(category_name)
    context.home_page_object.click_search_button()


@when('Results page: I select "{department_filter}"')
def step_impl(context, department_filter):
    context.home_page_object.select_filter_department(department_filter)


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

@when("Home page: I search for samsung from Electronics")
def step_impl(context):
    context.home_page_object.insert_search_value("samsung")
    context.home_page_object.choose_category("Electronics")
    context.home_page_object.click_search_button()

@when("Results page: I select Cell Phones & Accessories")
def step_impl(context):
    context.home_page_object.select_filter_department("Cell Phones & Accessories")

@when("Home page: I search for huawei from Electronics")
def step_impl(context):
    context.home_page_object.insert_search_value("huawei")
    context.home_page_object.choose_category("Electronics")
    context.home_page_object.click_search_button()

@when("Home page: I search for oppo from Electronics")
def step_impl(context):
    context.home_page_object.insert_search_value("oppo")
    context.home_page_object.choose_category("Electronics")
    context.home_page_object.click_search_button()

@when("Home page: I search for keyboard from Computers")
def step_impl(context):
    context.home_page_object.insert_search_value("keyboard")
    context.home_page_object.choose_category("Computers")
    context.home_page_object.click_search_button()

@when("Results page: I select Monitors")
def step_impl(context):
    context.home_page_object.select_filter_department("Monitors")

@when("Home page: I search for TV from Computers")
def step_impl(context):
    context.home_page_object.insert_search_value("TV")
    context.home_page_object.choose_category("Computers")
    context.home_page_object.click_search_button()

@when("Home page: I search for monitor from Computers")
def step_impl(context):
    context.home_page_object.insert_search_value("monitor")
    context.home_page_object.choose_category("Computers")
    context.home_page_object.click_search_button()

@when("Home page: I search for men smartwatch from All Departments")
def step_impl(context):
    context.home_page_object.insert_search_value("men smartwatch")
    context.home_page_object.choose_category("All Departments")
    context.home_page_object.click_search_button()

@when("Results page: I select Wearable Technology")
def step_impl(context):
    context.home_page_object.select_filter_department("Wearable Technology")

@when("Home page: I search for women smartwatch from All Departments")
def step_impl(context):
    context.home_page_object.insert_search_value("women smartwatch")
    context.home_page_object.choose_category("All Departments")
    context.home_page_object.click_search_button()

@when("Home page: I search for unisex smartwatch from All Departments")
def step_impl(context):
    context.home_page_object.insert_search_value("unisex smartwatch")
    context.home_page_object.choose_category("All Departments")
    context.home_page_object.click_search_button()

@when("Home page: I search for smartwatch from All Departments")
def step_impl(context):
    context.home_page_object.insert_search_value("smartwatch")
    context.home_page_object.choose_category("All Departments")
    context.home_page_object.click_search_button()





