from collections import Mapping, OrderedDict
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework.settings import api_settings
from rest_framework.exceptions import ValidationError
from rest_framework.fields import get_error_detail, set_value
from rest_framework.fields import SkipField
from users.decorators import UserBasicDecorators
from job.serializers import MajorRelatedSerializers
from job.models import Major
from .models import Category, Post, POST_STATE

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

class PostSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    cover = serializers.ImageField()
    thumb = serializers.SerializerMethodField()
    body = serializers.CharField()
    intro = serializers.CharField()
    state = serializers.ChoiceField(choices=POST_STATE, default=-1)
    publish_time = serializers.DateTimeField(required=False)
    categories = CategoryRelatedSerializers(many=True, queryset=Category.objects.all())
    majors = MajorRelatedSerializers(many=True, queryset=Major.objects.all())
    user = UserBasicDecorators(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'cover', 'thumb', 'body', 'intro', 'state', 'publish_time', 'categories', 'majors', 'user')

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

        # convert majors from string to list
        majors = None
        try:
            majors = data['majors'].replace('"', '').split(',')
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
            
            # if field is 'majors', set primitive_value to majors. if majors, skip to next loop
            if field.field_name == 'majors':
                if majors is not None:
                    primitive_value = majors
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

