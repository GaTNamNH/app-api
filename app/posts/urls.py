from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostViewset

posts = routers.SimpleRouter()
posts.register('', PostViewset)

urlpatterns = [
    path('v1/', include(posts.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)

