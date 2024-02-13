from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register(r 'books', views.Bookviewset)