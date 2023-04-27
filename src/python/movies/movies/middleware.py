import threading

class RequestCounterMiddleware:
    _lock = threading.Lock()
    counter = 0
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        return response
    
    def process_request(self, request):
        print("CALL TO MIDDLEWARE")
        with self._lock:
            self.counter += 1