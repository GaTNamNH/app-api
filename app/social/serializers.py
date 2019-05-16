from rest_framework import serializers

class OAuth2TokenInputSerializer(serializers.Serializer):
    access_token = serializers.CharField(help_text='the access token has been retrieve from facebook')

