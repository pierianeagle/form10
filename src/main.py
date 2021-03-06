import logging

from flask import Flask, request
from waitress import serve

from endpoints import api, api_document, api_predict


logging.basicConfig(
    format="[%(levelname)s %(module)s] %(asctime)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def home():
    logger.info("Access to landing page")

    return "Hi, I'm a landing page."


@app.route("/api", methods=["POST"])
def route_43():
    logger.info("Access to api endpoint.")

    data = request.get_json()
    res = api.get_estimated_sentiment(data)

    return res


@app.route("/api/document", methods=["POST"])
def route_66():
    logger.info("Access to api/document endpoint.")

    data = request.get_json()
    res = api_document.get_estimated_sentiment(data)

    return res


@app.route("/api/predict", methods=["POST"])
def route_12():
    logger.info("Access to api/predict endpoint.")

    data = request.get_json()
    res = api_predict.get_prediction(data)

    return res


serve(app, port=50055, host="0.0.0.0")
