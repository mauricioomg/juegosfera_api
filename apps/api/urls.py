from django.urls import path, include
from .router import router


app_name = 'api' 

urlpatterns = [
    path('api/', include(router.urls)),
]