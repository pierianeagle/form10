import logging
import pickle
import json

import numpy  as np
import pandas as pd


# initialise the logger 
logger = logging.getLogger(__name__)

# # see line 68
# load the model
with open(r'../resources/models/superduper.pkl', 'rb') as f:
    model = pickle.load(f)

# load the database
# # maybe this should be in mongo with internal html fragments
# with open('./resources/data/data.csv', 'r') as f:
#     df = pd.read_csv(f, index_col=0)

def build_json(n_results):
    """Build a skeleton json object to be filled.
    
    Args:
        n_results: The number of results to be returned.
    """
    skele = {}
    skele['results'] = []

    # the number of results 
    for i in range(n_results):
        result = {}
        result['filing_date'] = None
        result['sentiment'] = None

        skele['results'].append(result)
    return skele


def get_estimated_sentiment(req):
    """Esimate the sentiment of the requested documents.
    
    Args:
        req: The posted json.
    """
    logger.info("Checking the ticker.")
    ticker = req['ticker']

    # # make these optional using try except statements
    logger.info("Checking the start date")
    date_from = req['date_from']

    logger.info("Checking the end date")
    date_to = req['date_to']

    # # search the database for the relevant data
    # # determine the number of results
    results = [1, 2, 3]

    # build the skeleton json response
    logger.info("Building the skeleton json response.")
    res = build_json(len(results))

    logger.info("Filling the json response.")
    for i in range(len(results)):
        # # this should actually pull something from the database
        # # the database should be updated as new filings come in
        res['results'][i]['filing_date'] = "1997-05-10"
        # # predictions should be done beforehand since they would take ages
        # # in real life
        # # get the esimated sentiments from the database
        res['results'][i]['sentiment']   = model.predict(results)[i]

    logger.info("Returning the json response.")
    return json.dumps(res)
