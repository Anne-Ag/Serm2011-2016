"""
import .doc in list with associated fname list
"""
# as doc
import os, re
import docx2txt, textract
from pandas import DataFrame
# walk tree
def list_files(dirpath):
    """
    Walk all files in directory 'dir' and subdirectories
    return filenames in list
    """
    r = []
    for root, dirs, files in os.walk(dirpath):
        for name in files:
            r.append(os.path.join(root, name))
    return r

# denoise fnames
pat = re.compile("~")
dpath = "SERMON_CLEAN"
fnames = sorted(list_files(dpath))
error_idx = []
fnames_nonoise = []
for i, fname in enumerate(fnames):
    tmp = fname.split("/")[-1]
    if pat.match(tmp):
        error_idx.append(i)
    else:
        fnames_nonoise.append(fname)

# classify file type and remove metadata
DATA = []
pat1 = re.compile(r"% \S+")
pat2 = re.compile(r"\n+")
i = 0
for fname in fnames_nonoise:
    print("file {}".format(i))
    i += 1
    filetype = fname.split(".")[-1]
    if filetype == "doc":
        text = textract.process(fname).decode('utf-8')
    elif filetype == "docx":
        text = docx2txt.process(fname)
    else:
        print(fname)# TODO read odt
    # remove metadata
    text = pat1.sub("",text)
    text = pat2.sub("\n",text)
    DATA.append([fname.split("/")[-1].split(".")[0], text])

DF = DataFrame(DATA)
DF.columns = ["id", "content"]
DF.to_csv("content.dat", index = False)
