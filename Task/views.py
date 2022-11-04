from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OperationSerializer 

class View(APIView):
    def get(self, *args, **kwargs):
        data={"slackUsername":'Livingstone',
        'backend':True,
        'age':18,
        'bio':'backend developer with big dreams'}
        return Response(data)


class OperationView(APIView):
   serializer_class= OperationSerializer
   
   
   def post(self, *args, **kwargs):
      serializers= self.serializer_class(data=self.request.data)
      if serializers.is_valid():
         x= serializers.validated_data['x']
         y= serializers.validated_data['y']
         op= serializers.validated_data['operation_type']
         if op == 'addition':
            result= x + y
            op_type= 'addition' 

         elif op == 'subtraction':
            result= x - y
            op_type= 'addition' 
         elif op == 'multiplication':
            result= x * y
            op_type= 'multiplication'
         else:
            result=op
            op_type=op
         return Response({'slackUsername':'Livingstone', 'result':result, 'operation_type': op_type}) 
