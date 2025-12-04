from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list',views.UsersListView,basename='list')

urlpatterns = [
    path('alloper/',views.UsersListView.as_view(),name='alloper'),
    path('allopers/<int:pk>',views.UpdateUserView.as_view(),name='allopers'),
    path('login/',views.LoginView.as_view(),name='login'),
    # path('bgh/', router.urls),
]
