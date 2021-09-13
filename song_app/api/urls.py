
from .views import main
from django.urls.conf import path


urlpatterns = [
    path('', main)
]