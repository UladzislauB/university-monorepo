import pickle
from django.contrib.staticfiles.storage import staticfiles_storage

# str = input()


def detecting_fake_news(var):
    load_model = pickle.load(open('/home/qwerty/PycharmProjects/news-api-site/fake_news_detect/final_model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])

    return prediction[0], prob[0][1]


# if __name__ == '__main__':
#     print(detecting_fake_news(str))
