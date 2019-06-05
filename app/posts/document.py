# from django.conf import settings
# from django_elasticsearch_dsl import DocType, Index, fields
# from .models import Post, Category
# from users.models import User

# # Name of the Elasticsearch index
# post = Index('post')

# post.settings(
#     number_of_shards=1,
#     number_of_replicas=0
# )

# @post.doc_type
# class PostDocument(DocType):
#     categories = fields.NestedField(properties={
#         'id': fields.IntegerField(),
#         'display_name': fields.TextField()
#     })
#     user = fields.NestedField(properties={
#         'id': fields.IntegerField(),
#         'username': fields.TextField(),
#         'first_name': fields.TextField(),
#         'last_name': fields.TextField(),
#         'image_thumb': fields.TextField(attr='image_thumb_to_string')
#     })
#     title = fields.TextField()
#     thumb = fields.TextField(attr='thumb_to_string')
#     publish_time = fields.TextField(fielddata=True)

#     class Meta:
#         model = Post # The model associated with this DocType
#         related_models = [Category, User]
#         # The fields of the model you want to be indexed in Elasticsearch
#         fields = [
#             'id',
#             'intro',
#             'is_active'
#         ]

#     def get_instances_from_related(self, related_instance):
#         return related_instance.post_set.all()
