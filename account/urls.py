
from django.urls import path,include
from account.views import RegistrationView,LoginView
urlpatterns = [
    
    path('register/',RegistrationView.as_view(),name='register'),
    path('',RegistrationView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login')
]
