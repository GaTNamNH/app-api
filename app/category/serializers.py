from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Category

class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'display_name')

class CategoryRelatedSerializers(serializers.RelatedField):

    class Meta:
        model = Category
        fields = ('id', 'display_name')
    
    def to_representation(self, value):
        return {
            'id': value.id,
            'display_name': value.display_name
        }

    def to_internal_value(self, data):
        ids = list(category.id for category in self.queryset)
        msg = None
        try:
            data = int(data)
            if not data in ids:
                msg = _('invalid category.')
        except:
            msg = _('invalid category.')
        if msg:
            raise ValidationError(msg)
        return data