from django.urls import path
from manage_shops import views

urlpatterns = [
    path('find_shops/', views.find_shops, name="find shops"),
]