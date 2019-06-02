from django.shortcuts import render
import json
from newsapi import NewsApiClient
from news.models import TopHeadline
from likes import services

newsapi = NewsApiClient(api_key='959ed0e9826742709ee20cbc5632d5d5')


# Create your views here.

def index(request):
    top_headlines = TopHeadline.objects.order_by('-publishedAt')[:6]
    pairs = []
    for i in range(6):
        pairs.append([top_headlines[i], services.is_fan(top_headlines[i], request.user)])
    context = {'top_headlines': pairs}
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
