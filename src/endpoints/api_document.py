import logging
import json

from models.bag_of_words import prep, bow


# initialise the logger 
logger = logging.getLogger(__name__)

def build_json_skele():
    """Build the json skeleton to be filled."""
    skele = {}
    skele['results'] = []

    return skele


def build_result_skele():
    """Build a result json skeleton to be filled"""
    skele = {}
    skele['sentiment'] = None

    return skele


def get_estimated_sentiment(req):
    """Esimate the sentiment of the requested documents.
    
    Args:
        req: The posted json.
    """
    logger.info("Checking the ticker.")
    ticker = req['ticker']

    logger.info("Checking the filing.")
    filing = req['document']

    # build the json response
    logger.info("Building the json response.")
    res = build_json_skele()

    # build and fill the result json
    logger.info("Building and filling the result json.")
    results = []

    # make the prediction on the fly
    results.append(bow(prep(filing)))

    # fill the json response
    logger.info("Filling the json response.")
    res['results'] = results

    logger.info("Returning the json response.")
    return json.dumps(res)
