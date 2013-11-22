import numpy as np
import pandas as pd
from sklearn.manifold import MDS
from sklearn.metrics.pairwise import euclidean_distances

df = pd.read_csv("prepared_data.csv")

