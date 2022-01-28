import json


# open the file
with open(r'../resources/data/loughran_mcdonald.json', 'r') as f:
    dictionary = json.loads(f.read())

print(dictionary.keys())
# make the lists of words lowercase
dictionary['Negative']    = [word.lower() for word in dictionary['Negative']]
dictionary['Positive']    = [word.lower() for word in dictionary['Positive']]
dictionary['Uncertainty'] = [word.lower() for word in dictionary['Uncertainty']]
dictionary['Ligitious']   = [word.lower() for word in dictionary['Litigious']]

# write the new file
with open(r'../resources/data/loughran_mcdonald_lower.json', 'w') as f:
    json.dump(dictionary, f)
