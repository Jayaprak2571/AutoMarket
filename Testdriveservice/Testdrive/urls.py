from django.urls import path,include
from .import views

urlpatterns = [
    path('test/',views.TestDriving.as_view(),name='test'),
    path('updatestatus/<int:pk>',views.UpdateTestDriving.as_view(),name='updatestatus'),
    # path('getdrives/<int:id>/<str:drive_status>',views.UpdateStatus.as_view(),name='getdrives'),
    path('getdrives/<int:id>/<int:vid>',views.UpdateStatus.as_view(),name='getdrives'),
    path('getuserdrives/<int:id>',views.GetAllUserDrives.as_view(),name='getdrives'),

]
