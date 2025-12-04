from django.shortcuts import render
from .models import CarImage, Car
from .serializers import CarSerializer, CarImageSerializer
from rest_framework import generics,viewsets,mixins
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .filters import ProductFilter
from rest_framework.throttling import ScopedRateThrottle

class AddCar(generics.ListAPIView,generics.CreateAPIView):
    permission_class =[AllowAny]
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'cars-list'

    
    # def initial(self, request, *args, **kwargs):
    #     if request.method == 'GET':
    #         self.throttle_scope = 'cars-list'



    # filter_backends = [DjangoFilterBackend]
    # filterset_class = ProductFilter

    # filter_fileds=['make','model']
    # search_fields =['year']
    # ordering_fields =['price']
    

class UpdateCar(generics.UpdateAPIView,generics.RetrieveAPIView,generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class=CarSerializer
    lookup_field ='pk'

class AddCarImage(generics.ListAPIView,generics.CreateAPIView):
    queryset = CarImage.objects.all()
    serializer_class=CarImageSerializer
                    
class UpdateCarImage(generics.UpdateAPIView,generics.RetrieveAPIView,generics.DestroyAPIView):
    queryset = CarImage.objects.all()
    serializer_class=CarImageSerializer
    lookup_field ='pk'


from django.db.models import Prefetch
class getCarUser(APIView):
    permission_class =[AllowAny]
    def get(self, request,sid):
        seller_id = sid
        queryset = Car.objects.filter(seller_id=seller_id)
            
        if not queryset.exists():
            return Response({'detail': 'No cars found for this user'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(queryset, many=True)
        return Response([serializer.data], status=status.HTTP_200_OK)


from django.forms.models import model_to_dict

class getUserCarImages(APIView):
    permission_class =[AllowAny]
    def get(self, request, sid,id):
            queryset =  CarImage.objects.filter(car__seller_id=sid,car_id=id)
            print(queryset)
            serializer = CarImageSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

























# import jwt
 
# class getCarUser(APIView):
#     # Remove IsAuthenticated permission if not depending on request.user
#     def get(self, request):
#         # Extract token from the Authorization header
#         import requests

#         # Step 1: Login and get tokens
#         login_url = "http://localhost:8000/users/login/"  # Adjust to your login endpoint
#         login_data = {
#             "email": "umeshe@gmail.com",
#             "password": "Umesh@123"
#         }

#         login_response = requests.post(login_url, data=login_data)
#         tokens = login_response.json()
#         print("Login Response:", tokens)
#         print('headers   111',request.headers)

#         access_token = tokens.get("access")  # ✅ Use access token
#         refresh_token = tokens.get("refresh")  # For later if needed

#         # Step 2: Call getcars with access token
#         getcars_url = "http://localhost:8001/cars/getcars/"
#         headers = {
#             "Authorization": f"Bearer {access_token}"
#         }

#         getcars_response = requests.get(getcars_url, headers=headers)
#         print("GetCars Response:", getcars_response.json())
#         print('headers ',request.headers)

#         auth_header = request.headers.get('Authorization')
#         print('auth_header',auth_header)
#         if not auth_header or not auth_header.startswith('Bearer '):
#             return Response({'detail': 'Authentication token required'}, status=status.HTTP_401_UNAUTHORIZED)
#         access_token = auth_header.split(' ')[1]
 
#         # Decode JWT and get user_id
#         try:
#             payload = jwt.decode(
#                 access_token,
#                 'django-insecure-d5mi025pbnj*)7csssb9xlq7ri&!!3%&cud+!k5xok=ebdq5',  # <-- use your actual SIGNING_KEY
#                 algorithms=['HS256']
#             )
#             seller_id = payload.get('user_id')
#             if not seller_id:
#                 return Response({'detail': 'user_id not found in token'}, status=status.HTTP_400_BAD_REQUEST)
#         except jwt.ExpiredSignatureError:
#             return Response({'detail': 'Token expired'}, status=status.HTTP_401_UNAUTHORIZED)
#         except jwt.InvalidTokenError:
#             return Response({'detail': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
 
#         # Query cars using seller_id extracted from JWT
#         queryset = Car.objects.filter(seller_id=seller_id)
#         print("Decoded seller_id from JWT:", seller_id)
#         print("Cars for user:", queryset)
 
#         if not queryset.exists():
#             return Response({'detail': 'No cars found for this user'}, status=status.HTTP_404_NOT_FOUND)
 
#         serializer = CarSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
 

