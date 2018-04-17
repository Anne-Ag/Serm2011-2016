"""

"""
import ast, re
import pandas as pd

def str2list(s):
    return ast.literal_eval(s)

def getallis(l,match):
    return [i for i, x in enumerate(l) if x == match]

# data
df = pd.read_csv("content_entities.dat", header = 0, index_col = None)

fnames = df["id"].tolist()
entities = df["NE"].tolist()

idx = 0
entity = entities[idx]
#print(entity)

pat1 = r"\[\]\,*"
entity = re.sub(pat1,"",entity)
entity = re.sub(r" +"," ",entity)
entity = re.sub(r"\, \]",r"]",entity)
#print(entity)

M = re.findall(r"I-PER\(\[(.*?)\]\)\, ",entity)
#M = re.findall(r"I-PER\(\[ \]\)",entity)
for m in M:
    print(m)

"""
#pat = r"^.*\['(.*)'\].*$"
pat = r"\[I-PER\((.*)\)+?\]"

idx = 0
entity = entities[idx]
entity = entity[1:-1]
print(len(entity))
print()
m = re.findall(pat, entity)
print(m)
"""

"""
>>> import re
>>> s = u'abcde(date=\'2/xc2/xb2\',time=\'/case/test.png\')'
>>> re.search(r'\((.*?)\)',s).group(1)
u"date='2/xc2/xb2',time='/case/test.png'"
"""
