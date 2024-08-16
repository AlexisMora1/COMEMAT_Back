from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class Course_List_DB(APIView):
    def get(self, request):
        print(request)
        data = [
            {
                'name': 'pedro',
                'saludo': 'hey'
            }
        ]
        return Response(data)
    
    def post(self, request):
        request_data = request.data
        print('recibimos: ', request_data)

        return Response({'data':request_data})