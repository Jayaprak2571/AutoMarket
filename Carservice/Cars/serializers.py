from rest_framework import serializers
from .models import Car, CarImage

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields ='__all__'
        # def create(self, validated_data):
        #     validated_data['password']=make_password(validated_data.get('password'))
        #     return super().create(validated_data)
        
        # def update(self, instance, validated_data):
        #     password = validated_data.pop('password',None)
        #     if password:
        #         instance.password = make_password(password)
        #         for attr, value in validated_data.items():
        #             setattr(instance,attr,value)
        #             instance.save()
        #             return instance
        

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarImage
        fields = ['id','image','car']
        #fields ="__all__"
    
    