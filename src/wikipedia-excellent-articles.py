import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Import TSV file using Pandas
# TSV -> Tab Separated Values
df = pd.read_table('../data/gottron-excellent/out.gottron-excellent_trimmed', sep='\t', header=None)
G = nx.from_pandas_dataframe(df, 0, 1)
nx.draw(G)
plt.show()
