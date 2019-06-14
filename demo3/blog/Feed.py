from django.contrib.syndication.views import Feed
from .models import Article
class ArticleFeed(Feed):
    title="yj的个人博客"
    description="介绍一些精彩内容"
    link="/"


    def items(self):
        return Article.objects.all().order_by("-create_time")[:5]

    def item_title(self,item):
        return item.title

    def item_description(self, item):
        return item.body[:30]

    def item_link(self,item):
        return "/single/%s"%(item.id)

