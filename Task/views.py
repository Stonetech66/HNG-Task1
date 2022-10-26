from rest_framework.views import APIView
from rest_framework.response import Response

class View(APIView):
    def get(self, *args, **kwargs):
        data={"slackUsername":'Livingstone',
        'backend':True,
        'age':18,
        'bio':'backend developer with big dreams'}
        return Response(data)