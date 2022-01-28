import sys
import json

# hacky, don't like it
sys.path.append('./models')
from preprocess import preprocess


# read the dictionary
with open(r'../resources/data/loughran_mcdonald_lower.json', 'r') as f:
    dictionary = json.loads(f)


def bag_of_words(filing):
    """Return the Loughran McDonald sentiment counts."""
    lemmatized = preprocess(filing)

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
