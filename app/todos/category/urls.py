from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from ..views import CategoryViewset

router = routers.SimpleRouter()
router.register(r'', CategoryViewset)

urlpatterns = [
    path('v1/', include(router.urls)),
]
