import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import MDS
from sklearn.metrics.pairwise import euclidean_distances
import sys

def party_color(party):
  party = party.upper()
  if party == 'V':
    return '#D90000'
  elif party == 'S':
    return '#FF0000'
  elif party == 'MP':
    return '#0DFF5B'
  elif party == 'C':
    return '#078C32'
  elif party == 'FP':
    return '#2977E8'
  elif party == 'M':
    return '#290CE8'
  elif party == 'KD':
    return '#1111E8'
  elif party == 'SD':
    return '#704805'


df = pd.read_csv(sys.argv[1])
vote_columns = [c for c in df.columns if c != 'voter' and c != 'party' and c != 'name']

distances = euclidean_distances(df[vote_columns].values)
mds = MDS(dissimilarity="precomputed").fit_transform(distances)

plt.figure(figsize = (8, 5))
plt.plot(mds[:, 0], mds[:, 1], '.', alpha = 0)

for voter in enumerate(df['party']):
  plt.annotate(voter[1], 
      (mds[voter[0], 0], mds[voter[0],1]), 
      color = party_color(voter[1]),
      horizontalalignment = 'center', 
      verticalalignment = 'center')

plt.setp(plt.gca().get_yaxis(), visible = False)
plt.setp(plt.gca().get_xaxis(), visible = False)
plt.savefig(sys.argv[1] + ".png") 

