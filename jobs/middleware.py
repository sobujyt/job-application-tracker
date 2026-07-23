from datetime import datetime


class RequestLoggerMiddleware:
    """Custom middleware that logs the time, HTTP method, and path of every request."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        time_str = datetime.now().strftime("%Y-%m-%d %I:%M %p")
        print("---------------------------------")
        print(f"Time   : {time_str}")
        print(f"Method : {request.method}")
        print(f"Path   : {request.path}")
        print("---------------------------------")

        response = self.get_response(request)
        return response
