import atexit
import requests
from pact import Consumer, Provider

# Pact mock service will run locally
pact = Consumer('QA_Automation_Consumer').has_pact_with(
    Provider('ProductService'),
    pact_dir='contracts/pacts',   # Save pact JSON here
    log_dir='logs'                # Save logs here
)
pact.start_service()
atexit.register(pact.stop_service)

def test_get_products_contract():
    # Define expected interaction
    expected = [
        {"id": 1, "title": "Test Product", "price": 19.99, "category": "electronics"}
    ]

    (pact
     .given('Products exist')
     .upon_receiving('a request for all products')
     .with_request('get', '/products')
     .will_respond_with(200, body=expected))

    with pact:
        # Call the Pact mock server instead of real API
        result = requests.get(pact.uri + '/products')
        assert result.status_code == 200
        assert result.json() == expected
