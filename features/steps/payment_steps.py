import requests
from behave import when, then

@when('I send a payment request with "{data_key}" data')
def step_when_payment(context, data_key):
    url = context.env_config["mocks"]["payment"]
    payment_data = context.test_data["payments"][data_key]
    context.response = requests.post(url, json=payment_data)

@then("the payment response should indicate success")
def step_then_payment_success(context):
    json_response = context.response.json()
    assert json_response["status"] == "success", f"Expected success but got {json_response}"

@then("the payment response should indicate failure")
def step_then_payment_failure(context):
    json_response = context.response.json()
    assert json_response["status"] == "failed", f"Expected failed but got {json_response}"
