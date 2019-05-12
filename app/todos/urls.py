from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TodoViewset

router = routers.SimpleRouter()
router.register('', TodoViewset)

urlpatterns = [
    path('v1/', include(router.urls)),
    re_path(r'^category/', include('todos.category.urls')),
    re_path(r'^tag/', include('todos.tag.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
