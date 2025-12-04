from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

# router = DefaultRouter()
# router.register()

urlpatterns =[
    path('addcars/',views.AddCar.as_view(),name='addcars'),
    path('updatecar/<int:pk>',views.UpdateCar.as_view(),name='updatecar'),
    path('addcarimages/',views.AddCarImage.as_view(),name='addcarimages'),
    path('updatecarimages/<int:pk>',views.UpdateCarImage.as_view(),name='updatecarimages'),
    path('getcars/<int:sid>',views.getCarUser.as_view(),name='getcars'),
    path('getusercarimages/<int:sid>/<int:id>',views.getUserCarImages.as_view(),name='getusercarimages'),

]

'''
first add cars will get all vehicle and user ids
getusercarimages  will get images binded with user and vehicle
'''