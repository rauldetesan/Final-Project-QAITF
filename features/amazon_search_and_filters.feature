Feature: Test the search and filters functionality in the homepage of amazon

  Background:
    Given Home page: I am on amazon homepage

  @T1 @TestAll
  Scenario Outline: Check that the user can make a simple search in the amazon homepage and apply several filters on returned results page
    When Home page: I search for "<product_name>" from "<category_name>"
    When Results page: I select "<department_filter>"
    When Results page: I select $200 & Above from Price
    When Results page: I select on Avg. Customer Review four stars & Up
    When Results page: I select condition New
    When Results page: I select Availability
    Then Results page: I navigate back to homepage

    @cellphones
    Examples:
      | product_name |  category_name   | department_filter          |
      | samsung      |  Electronics     | Cell Phones & Accessories  |
      | huawei       |  Electronics     | Cell Phones & Accessories  |
      | oppo         |  Electronics     | Cell Phones & Accessories  |
      | motorola     |  Electronics     | Cell Phones & Accessories  |

    @electronics
    Examples:
      | product_name |  category_name   | department_filter |
      | keyboard     |  Computers       | Monitors          |
      | TV           |  Computers       | Monitors          |
      | monitor      |  Computers       | Monitors          |

    @wearables
    Examples:
      | product_name      |  category_name   | department_filter     |
      | men smartwatch    |  All Departments | Wearable Technology   |
      | women smartwatch  |  All Departments | Wearable Technology   |
      | unisex smartwatch |  All Departments | Wearable Technology   |
      | smartwatch        |  All Departments | Wearable Technology   |

  @T2 @TestAll
  Scenario: Check that the user can make a specific search on the amazon homepage
    When Home page: I search for samsung from Electronics
    When Results page: I select Cell Phones & Accessories
    When Results page: I select $200 & Above from Price
    When Results page: I select on Avg. Customer Review four stars & Up
    When Results page: I select condition New
    When Results page: I select Availability
    Then Results page: I navigate back to homepage

  @T3 @TestAll
  Scenario: Check that the user can make a specific search on the amazon homepage
    When Home page: I search for huawei from Electronics
    When Results page: I select Cell Phones & Accessories
    When Results page: I select $200 & Above from Price
    When Results page: I select on Avg. Customer Review four stars & Up
    When Results page: I select condition New
    When Results page: I select Availability
    Then Results page: I navigate back to homepage

  @T4 @TestAll
  Scenario: Check that the user can make a specific search on the amazon homepage
    When Home page: I search for oppo from Electronics
    When Results page: I select Cell Phones & Accessories
    When Results page: I select $200 & Above from Price
    When Results page: I select on Avg. Customer Review four stars & Up
    When Results page: I select condition New
    When Results page: I select Availability
    Then Results page: I navigate back to homepage

  @T5 @TestAll
  Scenario: Check that the user can make a specific search on the amazon homepage
    When Home page: I search for motorola from Electronics
    When Results page: I select Cell Phones & Accessories
    When Results page: I select $200 & Above from Price
    When Results page: I select on Avg. Customer Review four stars & Up
    When Results page: I select condition New
    When Results page: I select Availability
    Then Results page: I navigate back to homepage

  @T6 @TestAll
  Scenario: Check that the user can make a specific search on the amazon homepage
    When Home page: I search for keyboard from Computers
    When Results page: I select Monitors
    When Results page: I select $200 & Above from Price
    When Results page: I select on Avg. Customer Review four stars & Up
    When Results page: I select condition New
    When Results page: I select Availability
    Then Results page: I navigate back to homepage

  @T7 @TestAll
  Scenario: Check that the user can make a specific search on the amazon homepage
    When Home page: I search for TV from Computers
    When Results page: I select Monitors
    When Results page: I select $200 & Above from Price
    When Results page: I select on Avg. Customer Review four stars & Up
    When Results page: I select condition New
    When Results page: I select Availability
    Then Results page: I navigate back to homepage

  @T8 @TestAll
  Scenario: Check that the user can make a specific search on the amazon homepage
    When Home page: I search for monitor from Computers
    When Results page: I select Monitors
    When Results page: I select $200 & Above from Price
    When Results page: I select on Avg. Customer Review four stars & Up
    When Results page: I select condition New
    When Results page: I select Availability
    Then Results page: I navigate back to homepage

  @T9 @TestAll
  Scenario: Check that the user can make a specific search on the amazon homepage
    When Home page: I search for men smartwatch from All Departments
    When Results page: I select Wearable Technology
    When Results page: I select $200 & Above from Price
    When Results page: I select on Avg. Customer Review four stars & Up
    When Results page: I select condition New
    When Results page: I select Availability
    Then Results page: I navigate back to homepage

  @T10 @TestAll
  Scenario: Check that the user can make a specific search on the amazon homepage
    When Home page: I search for women smartwatch from All Departments
    When Results page: I select Wearable Technology
    When Results page: I select $200 & Above from Price
    When Results page: I select on Avg. Customer Review four stars & Up
    When Results page: I select condition New
    When Results page: I select Availability
    Then Results page: I navigate back to homepage

  @T11 @TestAll
  Scenario: Check that the user can make a specific search on the amazon homepage
    When Home page: I search for unisex smartwatch from All Departments
    When Results page: I select Wearable Technology
    When Results page: I select $200 & Above from Price
    When Results page: I select on Avg. Customer Review four stars & Up
    When Results page: I select condition New
    When Results page: I select Availability
    Then Results page: I navigate back to homepage

  @T12 @TestAll
  Scenario: Check that the user can make a specific search on the amazon homepage
    When Home page: I search for smartwatch from All Departments
    When Results page: I select Wearable Technology
    When Results page: I select $200 & Above from Price
    When Results page: I select on Avg. Customer Review four stars & Up
    When Results page: I select condition New
    When Results page: I select Availability
    Then Results page: I navigate back to homepage