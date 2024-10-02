from django.urls import path
from . import views

urlpatterns = [
    path('centers/', views.get_training_centers, name='get_centers'),
    path('centers/create/', views.create_training_center, name='create_center'),
]