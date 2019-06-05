from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CategoryViewset

categories = routers.SimpleRouter()
categories.register('', CategoryViewset)

urlpatterns = [
    path('v1/', include(categories.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
