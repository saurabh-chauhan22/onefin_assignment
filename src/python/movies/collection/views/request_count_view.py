from rest_framework.views import APIView
from rest_framework.response import Response

from movies.middleware import RequestCounterMiddleware 

class RequestCounterView(APIView):
    '''
    Request count api view to get count of request made to the server
    '''
    def get(self, request):
        '''
        Get the no of request made to the server
        '''
        return Response({"requests": RequestCounterMiddleware._counter})
    
    def post(self, request):
        '''
        Post will reset the counter to 0 
        '''
        with RequestCounterMiddleware._lock:
            RequestCounterMiddleware._counter = 0
        return Response({"message": "request count reset successfully"})