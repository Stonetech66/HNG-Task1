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
      
         x= serializer.get('x') 
         y= serializer.get('y') 
         op= serializer.get('operation_type') 
         if op == 'addition':
            result= x + y
            op_type= 'addition' 

         elif op == 'subtraction':
            result= x - y
            op_type= 'subtraction' 
         elif op == 'multiplication':
            result= x * y
            op_type= 'multiplication'
         else:
      
            import openai

            openai.api_key = config("OPENAI_API_KEY")

 

            response = openai.Completion.create(
            model="text-davinci-002",
            prompt=op,
            temperature=0,
            max_tokens=100,
            ) 

            F=['addition', 'plus', 'add', '+', '-', 'minus', 'subtract', 'subtraction', 'multiply', 'multiplication', '*'] 
            for i in F:
               if i in op:
                  if i== 'add' or 'addition' or 'plus' or '+':
                     result=response['choices'][0]['texts'] 
                     op_type='addition' 
                  elif i== 'minus' or 'subtraction' or 'subtract' or '-':
                     result=response['choices'][0]['texts'] 
                     op_type='subtraction' 
                  elif i== '*' or 'multiplication' or 'multiply':
                     result=response['choices'][0]['texts'] 
                     op_type='multiplication' 
                  
         return Response({'slackUsername':'Livingstone', 'result':result, 'operation_type': op_type}) 
