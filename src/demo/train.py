import pickle

import numpy as np


class Oracle(object):
    """A person (such as a priestess) through whom a god was believed to speak."""

    def predict(self, x):
        """Predict the future.

        Args:
            x: Useless
        """
        return np.random.uniform(size=len(x))


oracle = Oracle()

with open(r"../../resources/models/superduper.pkl", "wb") as f:
    pickle.dump(oracle, f)
