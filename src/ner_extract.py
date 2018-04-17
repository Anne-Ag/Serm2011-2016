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
#for i, text in enumerate(content[:4]):
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
#DF_pos.to_csv("content_entities.dat", index = False)

# extract all occurrences of specific class at sentence level for each document
entity_class = "I-PER"
df = DF_pos
entities = df["NE"].tolist()
fname = df["id"]
res = []
for i, doc in enumerate(entities):
    for ii, sent in enumerate(doc):
        if sent:
            for entity in sent:
                if entity.tag == entity_class:
                    res.append([fname[i], ii, entity])

df_out = pd.DataFrame(res)
df_out.columns = ["fname","sentence", entity_class]
df_out.to_csv("content_{}.dat".format(entity_class), index = False)
