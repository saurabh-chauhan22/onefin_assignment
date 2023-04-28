
class RequestCounterMiddleware:
    '''
    Request count middleware to count the number of request made to all the api
    to the server
    '''
    def __init__(self, get_response):
        self.get_response = get_response
        self.counter = 0

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        return response
    
    def process_request(self, request):
        # print("CALL TO MIDDLEWARE")
        self.counter += 1
        # print(f"Count:{self.counter}")
        request.request_counter = self


    def get_request_count(self):
        return self.counter