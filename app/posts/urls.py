from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostViewset

router = routers.SimpleRouter()
router.register('', PostViewset)

urlpatterns = [
    path('v1/', include(router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns)
