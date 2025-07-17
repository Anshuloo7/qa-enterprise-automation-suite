import os
from behave import when, then
from utils.api_client import make_request
from utils.retry import retry

@when('I send a payment request with "{data_key}" data')
@retry(retries=3, delay=2)
def step_when_payment(context, data_key):
    url = os.getenv("PAYMENT_URL", context.env_config["mocks"]["payment"])
    payment_data = context.test_data["payments"][data_key]
    context.response = make_request(context, "post", url, json=payment_data)
    assert context.response.status_code == 200

@then("the payment response should indicate success")
@retry(retries=3, delay=2)
def step_then_payment_success(context):
    json_response = context.response.json()
    assert json_response["status"] == "success", f"Expected success but got {json_response}"

@then("the payment response should indicate failure")
@retry(retries=3, delay=2)
def step_then_payment_failure(context):
    json_response = context.response.json()
    assert json_response["status"] == "failed", f"Expected failed but got {json_response}"