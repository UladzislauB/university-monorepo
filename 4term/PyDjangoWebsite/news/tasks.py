from mysite.celery import app
import json
from fake_news_detect.prediction import detecting_fake_news
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from newsapi import NewsApiClient
from news.models import TopHeadline

news = NewsApiClient(api_key='959ed0e9826742709ee20cbc5632d5d5');


@periodic_task(run_every=crontab(), name="get_top_news", ignore_result=True)
def get_top_news():
    top_headlines_source = news.get_top_headlines(sources='google-news')
    encoded_headlines = json.dumps(top_headlines_source, sort_keys=True, indent=4)
    decoded_headlines = json.loads(encoded_headlines).get('articles')
    for i in range(10):
        temp = decoded_headlines[i]
        headline = TopHeadline(author=temp.get('author'), title=temp.get('title'), description=temp.get('description'),
                               url=temp.get('url'), urlToImage=temp.get('urlToImage'),
                               publishedAt=temp.get('publishedAt'))
        res = detecting_fake_news(headline.description)
        headline.is_true = res[0]
        headline.is_true_prob = res[1]

        if not TopHeadline.objects.filter(title=headline.title):
            headline.save()
    print("iteration")
