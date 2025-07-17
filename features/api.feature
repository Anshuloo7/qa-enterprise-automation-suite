Feature: Product Service API
  As a consumer of the Product Service
  I want to retrieve product information
  So that I can display products to users

  Scenario: Fetch all available products
    When I fetch the list of products
    Then I should receive a successful response
    And the response should contain one or more products

  Scenario: Create a new product
    When I add a new product with the following details
      | title        | price | category     |
      | Test Product | 29.99 | electronics  |
    Then I should receive a successful response
    And the response should include the product details
