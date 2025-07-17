import os
from behave import when, then
from utils.api_client import make_request
from utils.retry import retry

@when("I fetch the list of products")
@retry(retries=3, delay=2)
def step_when_fetch_products(context):
    base_url = os.getenv("BASE_URL", context.env_config["base_url"])
    context.response = make_request(context, "get", f"{base_url}/products")
    assert context.response.status_code == 200, f"Expected 200 but got {context.response.status_code}"

@then("I should receive a successful response")
@retry(retries=3, delay=2)
def step_then_successful_response(context):
    assert context.response.status_code == 200

@then("the response should contain one or more products")
@retry(retries=3, delay=2)
def step_then_validate_products(context):
    json_response = context.response.json()
    assert isinstance(json_response, list) and len(json_response) > 0, "Expected non-empty list"
    required_fields = ["id", "title", "price", "category"]
    for field in required_fields:
        assert field in json_response[0], f"Missing field: {field}"

@when("I add a new product with the following details")
@retry(retries=3, delay=2)
def step_when_add_product(context):
    base_url = os.getenv("BASE_URL", context.env_config["base_url"])
    data = context.table[0].as_dict()
    data["price"] = float(data["price"])
    context.posted_product = data  # Move BEFORE making the API call
    context.response = make_request(context, "post", f"{base_url}/products", json=data)
    assert context.response.status_code in [200, 201]

@then("the response should include the product details")
@retry(retries=3, delay=2)
def step_then_response_includes_details(context):
    json_response = context.response.json()
    for key, value in context.posted_product.items():
        assert str(json_response.get(key)) == str(value)