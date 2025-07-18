Feature: Payment Service Mock
  Scenario: Process a valid payment
    When I send a payment request with "valid_payment" data
    Then the payment response should indicate success


  Scenario: Process an invalid payment
  When I send a payment request with "invalid_payment" data
  Then the payment response should indicate failure
