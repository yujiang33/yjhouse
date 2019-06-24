from haystack import indexes
from .models import Blog  #第一个地方

class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return Blog  #第二个地方
    def index_queryset(self, using=None):
        return self.get_model().objects.all()