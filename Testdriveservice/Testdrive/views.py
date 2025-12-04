from django.shortcuts import render
from .models import TestDrive
from .serializers import TestDriveSerializer
from rest_framework import generics,mixins,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.throttling import ScopedRateThrottle


class TestDriving(generics.CreateAPIView,generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = TestDrive.objects.all()
    serializer_class = TestDriveSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'drives-list'




    



class UpdateTestDriving(generics.UpdateAPIView,generics.RetrieveAPIView,generics.DestroyAPIView):
    queryset = TestDrive.objects.all()
    serializer_class = TestDriveSerializer
    lookup_field ='pk'

class UpdateStatus(APIView):
    def put(self, request,id,vid):
        new_status = request.data.get('status')
        user_obj = TestDrive.objects.filter(user_id=id,status='Pending',vehicle_id=vid)
        new_user_obj = user_obj.update(status=new_status)
        updated_qs = TestDrive.objects.filter(user_id=id, vehicle_id=vid, status=new_status)
        serializer = TestDriveSerializer(updated_qs, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


   
class GetAllUserDrives(APIView):
    def get(self, request, id):
        try:
            user_obj = TestDrive.objects.filter(seller_id=id)
            print('user_obj',  user_obj)
            serializer_class = TestDriveSerializer(user_obj,many=True)
            print(serializer_class.data)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        except TestDrive.DoesNotExist:
            return Response({'message': 'TestDrives not found'}, status=404)
        
    
