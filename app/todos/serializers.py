from rest_framework import serializers
from django import forms
from .models import Todo, Category, Tag, LANGUAGE_CHOICES, STYLE_CHOICES

class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')

class TagSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'title')

class TodoSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    subject = serializers.CharField()
    content = serializers.CharField()
    timer = serializers.TimeField()
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    class Meta:
        model = Todo
        fields = '__all__'
