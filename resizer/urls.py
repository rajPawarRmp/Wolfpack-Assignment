from django.urls import path
from resizer.views import ResizeView

urlpatterns = [
    
    
    path('',ResizeView.as_view())
]
