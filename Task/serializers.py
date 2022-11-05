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

   
