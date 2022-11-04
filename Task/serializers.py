from rest_framework import serializers
from decouple import config
Operation_types=[
('addition','addition'),
('subtraction','subtraction'), 
('multiplication','multiplication') 
]

class OperationSerializer(serializers.Serializer):
   operation_type=serializers.ChoiceField(choices= Operation_types)
   x=serializers.IntegerField(required=False)
   y=serializers.IntegerField(required=False)

   def validate_operation_type(self, value):
     X =['addition', 'subtraction', 'multiplication']
     if value not in X:
      
      import openai

      openai.api_key = config("OPENAI_API_KEY")

 

      response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"Q: {value} ",
      temperature=0,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["\n"]
) 
      print(response) 
      return {'response':response, 'op':value} 
     return value 
