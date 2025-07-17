import requests

def make_request(context, method, url, **kwargs):
    # Log request details
    context.logger.info(f"REQUEST: {method.upper()} {url}")
    if "params" in kwargs:
        context.logger.info(f"Query Params: {kwargs['params']}")
    if "json" in kwargs:
        context.logger.info(f"Request Body: {kwargs['json']}")

    # Make the request
    response = requests.request(method, url, **kwargs)

    # Log response details
    context.logger.info(f"RESPONSE: Status {response.status_code}")
    context.logger.info(f"Response Body: {response.text}")

    return response
