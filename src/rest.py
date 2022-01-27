import logging

from flask import Flask, request
from waitress import serve

import sentiment_analysis as sa


logging.basicConfig(
    format='[%(levelname)s %(module)s] %(asctime)s - %(message)s',
    level = logging.INFO
)

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/')
def home():
    logger.info("Access to landing page")

    return "Suck on my big fat landing page."


@app.route('/api', methods=['POST'])
def do_sentiment_analysis():
    logger.info("Access to api endpoint.")

    data = request.get_json()
    response = sa.get_estimated_sentiment(data)

    return response


serve(app, port=50055, host='0.0.0.0')
