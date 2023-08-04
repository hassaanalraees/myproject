from .views import HomeView,panorama_view
from django.urls import path

urlpatterns = [
    path('panorama/', panorama_view, name='panorama'),
    path('panorama1/', HomeView.as_view(), name='home'),
]