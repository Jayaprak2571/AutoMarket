from rest_framework import serializers
from .models import TestDrive

class TestDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model=TestDrive
        fields=['id','seller_id','user_id','vehicle_id','scheduled_date','status']
        #fields ='__all__'
        
        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            request = self.contex.get('request',None)
            print("request",request)
            if request and not getattr(request.user,'is_superuser',False):
                self.fields.pop('status')