from articles.models import Article
from django.views.generic import ListView


class ArticleListView(ListView):
    model = Article
    template = 'articles/news.html'

    def articles_list(self):
        ordering = '-published_at'
        articles = Article.objects.order_by(ordering)
        context = {'articles': articles}
        return context


