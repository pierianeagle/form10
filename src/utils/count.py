import os
import sys
import json

# hacky, don't like it
# run util from within the folder
sys.path.append('../')
from models.bag_of_words import bag_of_words


# read the dictionary
with open(r'../resources/data/loughran_mcdonald_lower.json', 'r') as f:
    dictionary = json.loads(f)

input_path  = r'../resources/data/filings'
output_path = r'../resources/data/counts'

for file_name in os.listdir(input_path):
    # read the filing
    with open(os.path.join(input_path,  file_name), 'r') as f:
        filing = f.read()

    # write the counts
    with open(os.path.hoin(output_path, file_name), 'w') as f:
        json.dump(bag_of_words(file_name), f)
