"""
Non-zero sentiment scores for all verbs
"""
import pandas as pd
import numpy as np

# verb-pronoun PMI
df = pd.read_csv("pmi.dat", header = 0, index_col = None)
words = df["word"].tolist()

# afinn verb scores
afinn = pd.read_csv("AFINN-da-32.txt", sep = "\t", header = 0, index_col = None)
a_sent = afinn["sentiment"].tolist()
a_sent0 = [x - (np.mean(a_sent)) for x in a_sent]
AFINN0 = dict(zip(afinn["word"].tolist(), a_sent0))
res = np.zeros(len(words))
for i, word in enumerate(words):
    res[i] = AFINN0.get(word,0.0)

# non-zero sentiment score index
idx = [i for i, x in enumerate(res) if x != 0.0]
df = df.ix[idx,:]
df["sentiment"] = [res[i] for i in idx]

df.to_csv("verb_sentiment.dat", index = False)
