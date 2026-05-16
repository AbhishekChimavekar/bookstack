from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        original_data = response.data

        if isinstance(original_data, dict):
            message = original_data.pop("detail", "An error occurred.")
            errors = original_data if original_data else {}
        elif isinstance(original_data, list):
            message = " ".join(str(i) for i in original_data)
            errors = {}
        else:
            message = str(original_data)
            errors = {}

        response.data = {
            "success": False,
            "message": str(message),
            "errors": errors,
        }

    return response