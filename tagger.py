"""
POS tagger for sermons in content.dat
"""
import pandas as pd
import nltk.data
from polyglot.text import Text

# data
DF = pd.read_csv("content.dat", header = 0, index_col = None)
content = DF["content"].tolist()
fnames = DF["id"].tolist()

tokenizer = nltk.data.load("tokenizers/punkt/norwegian.pickle")
DATA_pos = []
i = 0
for i, text in enumerate(content):
    print("file {}".format(i))
    # sentence disambiguation
    sents = tokenizer.tokenize(text)
    # POS
    text_pos = []
    for blob in sents:
        textblob = Text(blob, hint_language_code='da')
        if textblob.pos_tags:
            text_pos.append(textblob.pos_tags)
    DATA_pos.append([fnames[i],text_pos])

DF_pos = pd.DataFrame(DATA_pos)
DF_pos.columns = ["id", "POS"]
DF_pos.to_csv("content_pos.dat", index = False)
