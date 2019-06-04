from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from django.views import View
import json
from newsapi import NewsApiClient
from news.models import TopHeadline
from likes import services

newsapi = NewsApiClient(api_key='959ed0e9826742709ee20cbc5632d5d5')


# Create your views here.

def index(request):
    top_headlines = TopHeadline.objects.order_by('-publishedAt')
    paginator = Paginator(top_headlines, 6)

    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    page_headlines = page_obj.object_list
    pairs = []
    for i in range(len(page_obj)):
        pairs.append([page_headlines[i], services.is_fan(page_headlines[i], request.user)])
    context = {'top_headlines': pairs,
               'page_obj': page_obj}
    return render(request, "news/index.html", context)


def top_headlines(request):
    top_headlines_source = newsapi.get_top_headlines(sources='google-news')
    encoded_headlines = json.dumps(top_headlines_source, sort_keys=True, indent=4)
    decoded_headlines = json.loads(encoded_headlines).get('articles')
    for i in range(10):
        temp = decoded_headlines[i]
        headline = TopHeadline(author=temp.get('author'), title=temp.get('title'), description=temp.get('description'),
                               url=temp.get('url'), urlToImage=temp.get('urlToImage'),
                               publishedAt=temp.get('publishedAt'))

        if not TopHeadline.objects.filter(title=headline.title):
            headline.save()
    context = {'top_headlines': TopHeadline.objects.order_by('-publishedAt')[:6]}
    return render(request, "news/top_headlines.html", context)


def article(request, article_id):
    headline = TopHeadline.objects.get(id=article_id)
    context = {'headline': headline}
    return render(request, 'news/article.html', context)


class SearchView(View):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        founded_news = TopHeadline.objects.filter(Q(title__icontains=query) or Q(description__icontains=query))
        paginator = Paginator(founded_news, 6)

        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        page_headlines = page_obj.object_list
        pairs = []
        for i in range(len(page_obj)):
            pairs.append([page_headlines[i], services.is_fan(page_headlines[i], request.user)])
        context = {'top_headlines': pairs,
                   'page_obj': page_obj,
                   'flag': True,
                   'query': query}
        return render(self.request, 'news/index.html', context)


def favourites(request):
    favourites = request.user.topheadline_set.all()
    paginator = Paginator(favourites, 6)

    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    page_headlines = page_obj.object_list
    pairs = []
    for i in range(len(page_obj)):
        pairs.append([page_headlines[i], services.is_fan(page_headlines[i], request.user)])
    context = {'top_headlines': pairs,
               'page_obj': page_obj}
    return render(request, "news/index.html", context)