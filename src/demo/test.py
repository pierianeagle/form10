import pickle

import pandas as pd

from sklearn.metrics import mean_squared_error

# you need to import the class template, otherwise python won't know how to
# recreate the object from the serialization
from train import Oracle


# load the model
with open(r"../../resources/models/superduper.pkl", "rb") as f:
    model = pickle.load(f)

# load the data
df = pd.DataFrame(
    {
        "definitely_real_predictors": [1, 2, 3, 4, 5],
        "absolutely_not_made_up_targets": [0.01, 0.50, 0.99, 0.18, 0.43],
    }
)

X_test = df["definitely_real_predictors"]
y_test = df["absolutely_not_made_up_targets"]

# make some predictions
y_hat_test = model.predict(X_test)

# print the report
print(mean_squared_error(y_test, y_hat_test))
