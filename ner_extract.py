"""
NER for sermons in content.dat
"""

import pandas as pd
import nltk.data
from polyglot.text import Text

# data
DF = pd.read_csv("content.dat", header = 0, index_col = None)
content = DF["content"].tolist()
fnames = DF["id"].tolist()

tokenizer = nltk.data.load("tokenizers/punkt/norwegian.pickle")
DATA_ne = []
i = 0
for i, text in enumerate(content):
    print("file {}".format(i))
    # sentence disambiguation
    sents = tokenizer.tokenize(text)
    # NER1
    text_entities = []
    for blob in sents:
        textblob = Text(blob, hint_language_code='da')
        text_entities.append(textblob.entities)
        #if textblob.entities:
        #    text_entities.append(textblob.entities)
    DATA_ne.append([fnames[i],text_entities])


DF_pos = pd.DataFrame(DATA_ne)
DF_pos.columns = ["id", "NE"]
DF_pos.to_csv("content_entities.dat", index = False)
