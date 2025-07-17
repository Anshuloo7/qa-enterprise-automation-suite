import atexit
import requests
from pact import Consumer, Provider

pact = Consumer('QA_Automation_Consumer').has_pact_with(
    Provider('ProductService'),
    pact_dir='contracts/pacts',   # Save pact JSON here
    log_dir='logs'                # Save logs here
)
pact.start_service()
atexit.register(pact.stop_service)

def test_create_product_contract():
    # Expected request body
    request_body = {
        "title": "Test Product",
        "price": 29.99,
        "category": "electronics"
    }

    # Expected response body
    response_body = {
        "id": 101,
        "title": "Test Product",
        "price": 29.99,
        "category": "electronics"
    }

    # Define Pact interaction
    (pact
     .given('Product can be created')
     .upon_receiving('a request to create a product')
     .with_request('post', '/products', body=request_body)
     .will_respond_with(201, body=response_body))

    with pact:
        result = requests.post(pact.uri + '/products', json=request_body)
        assert result.status_code == 201
        assert result.json() == response_body
