from django.urls import path
from .views import reality_view

urlpatterns = [
    path('', reality_view, name='reality_view')
]