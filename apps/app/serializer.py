from .models import App
from rest_framework import serializers

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']