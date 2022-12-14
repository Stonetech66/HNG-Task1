from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OperationSerializer 
from decouple import config 

class View(APIView):
    def get(self, *args, **kwargs):
        data={"slackUsername":'Livingstone',
        'backend':True,
        'age':18,
        'bio':'backend developer with big dreams'}
        return Response(data)


class OperationView(APIView):
   
   
   
   def post(self, request, *args, **kwargs):
         
         try:
           x= request.data.get('x') 
           y= request.data.get('y') 
         except:
             pass
         op= request.data.get('operation_type') 
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
            prompt=f"they are numbers {op}", 
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            ) 

            F=['addition', 'plus', 'add', '+', '-', 'minus', 'subtract', 'subtraction', 'multiply', 'multiplication', '*'] 
            for i in F:
               if i in op:
                  if i== 'add' or i== 'addition' or i== 'plus' or i== '+':
      
                     op_type='addition' 
                  elif i== 'minus' or i== 'subtraction' or i== 'subtract' or i== '-':
                     
                     op_type='subtraction' 
                  elif i== '*' or i== 'multiplication' or i== 'multiply':
                     
                     op_type='multiplication'
                  try:
                     result=int(response['choices'][0]['text']) 
                  except:
                     result=response['choices'][0]['text'] 
         return Response({'slackUsername':'Livingstone', 'result':result, 'operation_type': op_type}) 
