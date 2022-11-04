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
      serializer= self.serializer_class(data=self.request.data)
      if serializer.is_valid():
         x= serializer.validated_data['x']
         y= serializer.validated_data['y']
         op= serializer.validated_data['operation_type']
         if op == 'addition':
            result= x + y
            op_type= 'addition' 

         elif op == 'subtraction':
            result= x - y
            op_type= 'subtraction' 
         elif op == 'multiplication':
            result= x * y
            op_type= 'multiplication'
         elif type(op) == dict:
            F=['addition', 'plus', 'add', '+', '-', 'minus', 'subtract', 'subtraction', 'multiply', 'multiplication', '*'] 
            for i in F:
               if i in op['op']:
                  if i== 'add' or 'addition' or 'plus' or '+':
                     result=op['response'] 
                     op_type='addition' 
                  elif i== 'minus' or 'subtraction' or 'subtract' or '-':
                     result=op['response'] 
                     op_type='subtraction' 
                  elif i== '*' or 'multiplication' or 'multiply':
                     result=op['response'] 
                     op_type='multiplication' 
         return Response({'slackUsername':'Livingstone', 'result':result, 'operation_type': op_type}) 
