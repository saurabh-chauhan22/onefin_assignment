from rest_framework.views import APIView
from rest_framework.response import Response

from ..token_authenticator import TokenAuthentication

class RequestCounterView(APIView):
    '''
    Request count api view to get count of request made to the server
    '''
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        '''
        Get the no of request made to the server
        '''
        request_counter = request.request_counter
        request_count = request_counter.get_request_count()
        return Response({"requests": request_count})
    
    def post(self, request):
        '''
        Post will reset the counter to 0 
        '''
        request_counter = request.request_counter
        request_counter.counter = 0
        return Response({"message": "request count reset successfully"})