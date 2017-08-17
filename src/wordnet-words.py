# Author: Rafael Pagliuca
# Created at: 2016-07-03
# Modified at: 2016-07-03

from __future__ import division
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from graphtools import *

# First we load the datafile and create a NetworkX object
# Source: http://konect.uni-koblenz.de/networks/wordnet-words
# Import TSV file using Pandas
# TSV -> Tab Separated Values
df = pd.read_table('../data/wordnet-words/out.wordnet-words', sep=' ', header=None)
G = nx.from_pandas_dataframe(df, 0, 1)

# Now we use the GraphTools class to generate some summary plots
gt = GraphTools(G)
gt.degree_distribution()
gt.cumulative_degree_distribution()
gt.assortativity()
gt.lorenz_curve()
gt.clustering_coefficient_distribution()
gt.distance_distribution()
