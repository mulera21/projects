from rest_framework import routers
from main import api_views as main_views

router = routers.DefaultRouter()
router.register(r'books', main_views.Bookviewset)