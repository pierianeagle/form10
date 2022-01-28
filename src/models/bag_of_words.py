import sys
import json

# hacky, don't like it
sys.path.append('./models')
from preprocess import clean, prep


# read the dictionary
with open(r'../resources/data/loughran_mcdonald_lower.json', 'r') as f:
    dictionary = json.load(f)


def bow(lemmatized):
    """Return the Loughran McDonald sentiment counts."""

    # build the skeleton json
    counts = {
        'Negative':    0,
        'Positive':    0,
        'Uncertainty': 0,
        'Litigious' :  0
    }

    # calculate the sentiment counts
    for word in lemmatized:
        if word in dictionary['Negative']:
            counts['Negative']    += 1
        if word in dictionary['Positive']:
            counts['Positive']    += 1
        if word in dictionary['Uncertainty']:
            counts['Uncertainty'] += 1
        if word in dictionary['Litigious']:
            counts['Litigious']   += 1

    return counts
