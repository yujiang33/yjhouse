from haystack import indexes
from .models import Article   # 引入要搜索文章

class ArticleIndex(indexes.SearchIndex,indexes.Indexable):
    text =indexes.CharField(document=True,use_template=True)
    def get_model(self):
        return Article
    def index_queryset(self,using=None):
        return self.get_model().objects.all()
