import requests
import json
import time
from allure_commons._allure import attach
from allure_commons.types import AttachmentType


def make_request(context, method, url, **kwargs):
    try:
        # Log request details
        context.logger.info(f"REQUEST: {method.upper()} {url}")
        if "params" in kwargs:
            context.logger.info(f"Query Params: {kwargs['params']}")
        if "json" in kwargs:
            context.logger.info(f"Request Body: {json.dumps(kwargs['json'], indent=2)}")

        start_time = time.time()
        response = requests.request(method, url, **kwargs)
        duration = round(time.time() - start_time, 2)

        # Log response details
        context.logger.info(f"RESPONSE: Status {response.status_code}")
        context.logger.info(f"Response Time: {duration}s")
        context.logger.info(f"Response Headers: {dict(response.headers)}")
        context.logger.info(f"Response Body: {response.text}")

        # Attach to Allure report
        attach(
            f"REQUEST:\n{method.upper()} {url}\n"
            f"Headers: {kwargs.get('headers', {})}\n"
            f"Query Params: {kwargs.get('params', {})}\n"
            f"Body: {json.dumps(kwargs.get('json', {}), indent=2)}\n\n"
            f"RESPONSE:\nStatus: {response.status_code}\n"
            f"Time: {duration}s\n"
            f"Headers: {dict(response.headers)}\n"
            f"Body: {response.text}",
            name="API Request & Response",
            attachment_type=AttachmentType.TEXT
        )

        # Save response for step-level debug
        context.response = response
        return response

    except requests.exceptions.RequestException as e:
        context.logger.error(f"Request failed: {e}", exc_info=True)
        attach(str(e), name="Request Exception", attachment_type=AttachmentType.TEXT)
        raise