from flask import Flask, request
from flask_cors import CORS
import os
from twittter import CheckUserExist
from vector import AccountDate, BuzzerDate, AverageTweets, BuzzerAverageTweets, WordCount, BuzzerWordCount
from dot_product import CosineSimilarity

app = Flask(__name__)
CORS(app)

@app.route('/check-buzzer', methods=['POST'])
def CheckBuzzer():
    username = request.json['username']
    if (CheckUserExist(user=username)):
        # User Vector
        user_vector = [AccountDate(user=username), AverageTweets(user=username), WordCount(user=username)]
        # Buzzer Vector
        buzzer_vector = [BuzzerDate(user=username), BuzzerAverageTweets(), BuzzerWordCount()]
        # Dot Product
        probability = round(CosineSimilarity(user_vector, buzzer_vector) * 100, 2)
        if (probability > 80):
            return str(probability) + '% - True'
        else:
            return str(probability) + '% - False'
    else:
        return 'Username tidak valid'

if __name__ == '__main__':
    app.run()