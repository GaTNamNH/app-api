from collections import Mapping, OrderedDict
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework.settings import api_settings
from rest_framework.exceptions import ValidationError
from rest_framework.fields import get_error_detail, set_value
from rest_framework.fields import SkipField
from category.serializers import CategoryRelatedSerializers
from category.models import Category
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    cover = serializers.ImageField()
    thumb = serializers.SerializerMethodField()
    body = serializers.CharField()
    intro = serializers.CharField()
    categories = CategoryRelatedSerializers(many=True, queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'title', 'cover', 'thumb', 'body', 'intro', 'categories')

    def get_thumb(self, obj):
        if obj.cover:
            return obj.thumb.url or None
        return None

    def to_internal_value(self, data):
        """
        Dict of native values <- Dict of primitive datatypes.
        """
        if not isinstance(data, Mapping):
            message = self.error_messages['invalid'].format(
                datatype=type(data).__name__
            )
            raise ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: [message]
            }, code='invalid')

        # convert categories from string to list
        categories = None
        try:
            categories = data['categories'].replace('"', '').split(',')
        except:
            pass

        ret = OrderedDict()
        errors = OrderedDict()
        fields = self._writable_fields

        for field in fields:
            validate_method = getattr(self, 'validate_' + field.field_name, None)
            primitive_value = field.get_value(data)

            # if field is 'categories', set primitive_value to categories. if categories, skip to next loop
            if field.field_name == 'categories':
                if categories is not None:
                    primitive_value = categories
                else:
                    continue
           
            try:
                validated_value = field.run_validation(primitive_value)
                if validate_method is not None:
                    validated_value = validate_method(validated_value)
            except ValidationError as exc:
                errors[field.field_name] = exc.detail
            except DjangoValidationError as exc:
                errors[field.field_name] = get_error_detail(exc)
            except SkipField:
                pass
            else:
                set_value(ret, field.source_attrs, validated_value)

        if errors:
            raise ValidationError(errors)

        return ret
