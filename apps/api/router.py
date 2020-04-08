from apps.api.viewsets import Product1Viewset
from rest_framework import routers
from apps.api import viewsets

router = routers.DefaultRouter()
router.register('product1', Product1Viewset)
router.register(r'users', viewsets.UserViewSet)

#