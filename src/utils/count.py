# # presumably in real life you have some sort of callback function that
# # processes new additions to the database
import os
import sys
import json

# hacky, don't like it
sys.path.append("./")
from models.bag_of_words import bow
from models.preprocess import clean, prep

# read the dictionary
with open(r"../resources/data/loughran_mcdonald_lower.json", "r") as f:
    dictionary = json.load(f)

input_path = r"../resources/data/filings"
output_path = r"../resources/data/counts"

for file_name in os.listdir(input_path):
    # read the filing
    with open(os.path.join(input_path, file_name), "r") as f:
        filing = f.read()

    # write the counts
    with open(os.path.join(output_path, file_name), "w") as f:
        json.dump(bow(prep(clean(filing))), f)
