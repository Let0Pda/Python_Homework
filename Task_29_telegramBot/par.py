import json
import requests


def ask_wikipedia_question(question):
    API_URL = 'https://7012.deeppavlov.ai/model'
    data = {'question_raw':  [question]}
    res = requests.post(API_URL, json=data, verify=False).json()
    return res[0][0]


def request_sentiment(message):
    API_URL = 'https://7015.deeppavlov.ai/model'
    data = {'x': [message]}
    res = requests.post(API_URL, json=data).json()
    santiment = res[0][0]
    return santiment


message = 'Хорошая погода'
question = 'быть или не быть'
santim = request_sentiment(message)
print(f'\n{santim}\n')
print(type(santim))
# resalt = ask_wikipedia_question(question)
# print(resalt)
