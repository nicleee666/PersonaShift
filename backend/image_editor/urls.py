from django.urls import path
from .views import home_view, image_upload_view

urlpatterns = [
    path('', home_view, name='home'),  # The root URL pattern
    path('upload/', image_upload_view, name='image_upload'),
]
