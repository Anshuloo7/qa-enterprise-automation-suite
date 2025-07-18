@ui
Feature: Search for a user in OrangeHRM

  Scenario: Search for an existing user
    Given I am on the OrangeHRM login page
    When I login with username "Admin" and password "admin123"
    Then I should see the dashboard
    When I search for user "Admin" in the Admin panel
    Then I should see user "Admin" in the search results