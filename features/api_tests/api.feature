@api @db
Feature: Product Service API with DB Validation
  As a QA Engineer
  I want to validate API responses and database state
  So that data integrity is ensured

  Scenario: Fetch all available products and validate DB
    When I fetch the list of products
    Then I should receive a successful response
    And the response should contain one or more products
    And the database should contain the same number of products
    And product with id 1 should exist in the database

  Scenario: Create a new product and validate DB
    When I add a new product with the following details
      | title        | price | category     |
      | Test Product | 29.99 | electronics  |
    Then I should receive a successful response
    And the response should include the product details
    And product with id 21 should exist in the database