from django_elasticsearch_dsl import DocType, Index
from .models import Todo

# Name of the Elasticsearch index
todo = Index('todos')

todo.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@todo.doc_type
class TodoDocument(DocType):
    class Meta:
        model = Todo # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'subject',
            'content'
        ]