from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import generics,mixins,viewsets
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login,logout
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .pagination import CustomPagination, CustomLimitOffsetPagination



class UsersListView(generics.ListAPIView,generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomLimitOffsetPagination

    def perform_create(self,serializer):
        password = serializer.validated_data.get('password')
        if password:
            serializer.validated_data['password']=make_password(password)
            serializer.validated_data['is_active']=True
            serializer.save()

class UpdateUserView(generics.UpdateAPIView,generics.RetrieveAPIView,generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field='pk'


# class LoginView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         queryset = User.objects.get(email=email)
#         print('queryset',queryset.username)
#         this_user = authenticate(request,username=queryset.username,password=password)
#         print('this_user',this_user)
#         if this_user is not None:
#             # login(request,this_user)
#             serializer_class=UserSerializer(queryset)
#             refresh = RefreshToken.for_user(this_user)
#             return Response({'user id':this_user.id,'message':'login successful','access':str(refresh.access_token),'refresh':str(refresh),'user':serializer_class.data},status=status.HTTP_200_OK)
#         return Response({'message':'login Failed'},status=status.HTTP_404_NOT_FOUND)


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)
        this_user = authenticate(username=user_obj.username, password=password)
        if this_user is not None:
            refresh = RefreshToken.for_user(this_user)
            serializer = UserSerializer(this_user)
            return Response({'user id': this_user.id,'message': 'login successful','access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': serializer.data
            }, status=200)
        return Response({'message': 'Invalid credentials'}, status=400)









