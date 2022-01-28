import os
import logging

# # see line 13
# # import pickle
import json
import re

import datetime as dt


# initialise the logger
logger = logging.getLogger(__name__)

# # allow different models to be selected
# with open(r'../resources/models/superduper.pkl', 'rb') as f:
#   super_duper = pickle.load(f)
# for i in range(len(results)):
#   res['results'][i]['sentiment'] = super_duper.predict(results)[i]


def build_json_skele():
    """Build the json skeleton to be filled."""
    skele = {}
    skele["results"] = []

    return skele


def build_result_skele():
    """Build a result json skeleton to be filled"""
    skele = {}
    skele["filing_date"] = None
    skele["sentiment"] = None

    return skele


def get_estimated_sentiment(req):
    """Esimate the sentiment of the requested documents.

    Args:
        req: The posted json.
    """
    logger.info("Checking the ticker.")
    ticker = req["ticker"]

    # # make these optional using try except statements
    logger.info("Checking the start date")
    date_from = dt.datetime.strptime(req["date_from"], "%Y-%m-%d")

    logger.info("Checking the end date")
    date_to = dt.datetime.strptime(req["date_to"], "%Y-%m-%d")

    # build the json response
    logger.info("Building the json response.")
    res = build_json_skele()

    # # this could be imported from a database module
    # # use mongodb?
    # search the database for the relevant data
    input_path = r"../resources/data/counts"

    # build and fill the result json
    logger.info("Building and filling the result json.")
    results = []

    # # the database should be check for new filings regularly
    # since predictions can be done beforehand, let's do that
    # they could take ages in real life
    for file_name in os.listdir(input_path):
        file_info = re.split("_|\.", file_name)
        file_date = dt.datetime.strptime(file_info[2], "%Y-%m-%d")

        if file_info[0] == ticker:
            if file_date > date_from:
                if file_date < date_to:
                    with open(os.path.join(input_path, file_name), "r") as f:
                        result = build_result_skele()

                        result["filing_date"] = file_date.strftime("%Y-%m-%d")
                        result["sentiment"] = json.load(f)

                        results.append(result)

    # fill the json response
    logger.info("Filling the json response.")
    res["results"] = results

    logger.info("Returning the json response.")
    return json.dumps(res)
