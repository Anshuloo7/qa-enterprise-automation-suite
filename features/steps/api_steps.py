from behave import when, then
from utils.api_client import make_request

@when("I fetch the list of products")
def step_when_fetch_products(context):
    base_url = context.env_config["base_url"]
    endpoint = "/products"
    context.response = make_request(context, "get", f"{base_url}{endpoint}")

@then("I should receive a successful response")
def step_then_successful_response(context):
    assert context.response.status_code == 200, \
        f"Expected status 200 but got {context.response.status_code}"

@then("the response should contain one or more products")
def step_then_validate_products(context):
    json_response = context.response.json()

    # Ensure response is a list
    assert isinstance(json_response, list), "Expected a list in response"
    assert len(json_response) > 0, "Expected at least one product"

    # Validate first product's structure
    first_product = json_response[0]
    required_fields = ["id", "title", "price", "category"]

    for field in required_fields:
        assert field in first_product, f"Missing field: {field}"

    # Additional check for field types
    assert isinstance(first_product["id"], int), "Product ID should be int"
    assert isinstance(first_product["title"], str), "Title should be string"
    assert isinstance(first_product["price"], (int, float)), "Price should be number"

@when("I add a new product with the following details")
def step_when_add_product(context):
    base_url = context.env_config["base_url"]
    endpoint = "/products"

    # Extract data from the Gherkin table
    data = context.table[0].as_dict()
    data["price"] = float(data["price"])  # Ensure price is numeric

    context.response = make_request(context, "post", f"{base_url}{endpoint}", json=data)
    context.posted_product = data

@then("the response should include the product details")
def step_then_response_includes_details(context):
    json_response = context.response.json()

    for key, value in context.posted_product.items():
        assert str(json_response.get(key)) == str(value), \
            f"Expected {key} to be {value}, got {json_response.get(key)}"
