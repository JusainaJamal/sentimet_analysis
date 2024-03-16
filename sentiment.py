import numpy as np
import pandas as pd
import pickle

# Load the pickled model
with open('best_model.pkl', 'rb') as f:
   model = pickle.load(f)
