from rest_framework import serializers
from .models import Todo

class TodoSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Todo
        fields = ('id', 'subject', 'content', 'timer', 'created')
