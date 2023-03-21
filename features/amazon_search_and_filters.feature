Feature: Test the search and filters functionality in the homepage of amazon

  Scenario: Check that the user can make a simple search in the amazon homepage
    Given Home page: I am on amazon homepage
    When Home page: I search for samsung from Electronics
    When Results page: I am on results page


  Scenario: Check that the user can apply several filters on returned results page
    When Results page: I select Cell Phones & Accessories
    When Results page: I click SAMSUNG on Featured Brands
    When Results page: I select $200 & Above from Price
    When Results page: I select on Avg. Customer Review four stars & Up
    When Results page: I select condition New
    When Results page: I select Availability
    Then Results page: I navigate back to homepage
