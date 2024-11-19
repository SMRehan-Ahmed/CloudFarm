from django.urls import path
from . import views
from .views import crop_fertilizer_prediction

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path("predict/", crop_fertilizer_prediction, name="predict"),

    
]
