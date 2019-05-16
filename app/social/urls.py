from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/(?:(?P<provider>[a-zA-Z0-9_-]+)/?)?$',
        views.SocialAuthenticationView.SocialAuthenticationViewSet.as_view(),
        name='login_social_jwt_user_v2'),
]
api_urlpatterns = urlpatterns