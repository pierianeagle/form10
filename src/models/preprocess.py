import nltk

from bs4 import BeautifulSoup

from nltk.tokenize import word_tokenize
from nltk.corpus import words, stopwords
from nltk.stem import WordNetLemmatizer


nltk.data.path.append(r"../resources/data/nltk_data/")


def clean(filing):
    """Remove html tags and special characters."""
    # parse html
    soup = BeautifulSoup(filing, "html.parser")

    for data in soup.body(["style", "script"]):
        # remove tags
        data.decompose()

    # convert a list of stripped lines into a list of stripped words
    snipped = " ".join(soup.body.stripped_strings).split()

    sparkling = ""
    for word in snipped:
        # turn the list back into a string, removing special characters and
        # whitespace from each word as we go
        sparkling += "".join(e for e in word if e.isalnum()) + " "

    return sparkling


# # WORDS SCOPING QUICK FIX!
def prep(filing, words=words):
    """Pre-process the filing."""
    # tokenize the string
    tokenized = word_tokenize(filing)

    # remove stop words
    filtered = [word for word in tokenized if word not in stopwords.words("english")]

    # remove not a words
    words = set(word.lower() for word in words.words())
    filtered = [word for word in filtered if word in words]

    # lemmatize the list
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in filtered]

    return lemmatized
