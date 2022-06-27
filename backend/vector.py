from twittter import User, Tweets
from complement import StringToDate, StringToDatetime, DateToDate
import os
import re

def AccountDate(user):
    user_data = User(username=user)['data']
    if (DateToDate(os.getenv('BUZZER_ACCOUNT_DATE')) <= StringToDate(user_data['created_at'].split('T')[0])):
        return (StringToDate(user_data['created_at'].split('T')[0]) - DateToDate(os.getenv('BUZZER_ACCOUNT_DATE'))).days
    else:
        return 1

def BuzzerDate(user):
    user_data = User(username=user)['data']
    if (StringToDate(user_data['created_at'].split('T')[0]) <= DateToDate(os.getenv('BUZZER_ACCOUNT_DATE'))):
        return (DateToDate(os.getenv('BUZZER_ACCOUNT_DATE')) - StringToDate(user_data['created_at'].split('T')[0])).days
    else:
        return 1

def AverageTweets(user):
    user_data = User(username=user)['data']
    tweets = Tweets(user_data['id'])
    tweet_constraint = min(min(10, int(os.getenv("LAST_TWEET_COUNT"))), tweets["meta"]["result_count"])
    tweet_time = 0
    tweet_count = 0
    while (tweet_count < tweet_constraint - 1):
        if (tweet_count == 0):
            tweet1 = tweets["data"][tweet_count]["created_at"].split('T')[0] + ' ' + tweets["data"][tweet_count]["created_at"].split('T')[1].split('.')[0]
        else:
            tweet1 = tweet2
        tweet2 = tweets["data"][tweet_count + 1]["created_at"].split('T')[0] + ' ' + tweets["data"][tweet_count + 1]["created_at"].split('T')[1].split('.')[0]
        tweet_time += ((StringToDatetime(tweet1) - StringToDatetime(tweet2)).total_seconds() / 3600)
        tweet_count += 1
    if (tweet_count == 0):
        return 0
    else:
        return tweet_time / tweet_count

def BuzzerAverageTweets():
    time, time_type = os.getenv('BUZZER_AVERAGE_TWEET').split(' ')
    time = int(time)
    if (time_type[0] == 'm'):
        time = time / 60
    return time

def WordCount(user):
    user_data = User(username=user)['data']
    tweets = Tweets(user_data['id'])
    tweet_constraint = min(min(10, int(os.getenv("LAST_TWEET_COUNT"))), tweets["meta"]["result_count"])
    word_count = 0

    for i in range(tweet_constraint):
        word_count += len(re.findall('[^a-zA-Z]' + os.getenv('WORD_TO_FIND').lower() + '[' + os.getenv('WORD_TO_FIND').lower() + ']*' + '[^a-zA-Z]', tweets['data'][i]['text'].lower()))
    return word_count

def BuzzerWordCount():
    return int(os.getenv('BUZZER_WORD_COUNT'))