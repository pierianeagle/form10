import os
import sys
import logging
# # see line 13
import pickle
import json
import re

# hacky, don't like it
sys.path.append("./demo")
from demo.train import Oracle

# initialise the logger
logger = logging.getLogger(__name__)

# # allow different models to be selected
with open(r'../resources/models/superduper.pkl', 'rb') as f:
    SuperDuper = pickle.load(f)


def build_json_skele():
    """Build the json skeleton to be filled."""
    skele = {}
    skele["results"] = []

    return skele


def build_result_skele():
    """Build a result json skeleton to be filled"""
    skele = {}
    skele["filing_date"] = None
    skele["prediction"] = None

    return skele


def get_prediction(req):
    """Make a prediction based upon the supplied document.

    Args:
        req: The posted json.
    """
    logger.info("Checking the ticker.")
    ticker = req["ticker"]

    logger.info("Checking the filing date.")
    filing_date = req["filing_date"]

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

    for file_name in os.listdir(input_path):
        file_info = re.split("_|\.", file_name)

        if file_info[0] == ticker:
            if file_info[2] == filing_date:
                    with open(os.path.join(input_path, file_name), "r") as f:
                        result = build_result_skele()

                        result["filing_date"] = file_info[2]
                        result["prediction"]  = SuperDuper.predict(os.path.join(input_path, file_name))

                        results.append(result)

    # fill the json response
    logger.info("Filling the json response.")
    res["results"] = results

    logger.info("Returning the json response.")
    return json.dumps(res)
