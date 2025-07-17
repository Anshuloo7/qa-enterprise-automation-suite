Feature: Example Test
  This is a sample feature to verify Behave setup.

  Scenario: Verify Behave is working
    Given I have Behave installed
    When I run the tests
    Then I should see the tests pass
