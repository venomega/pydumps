import sys

path = sys.argv[-1]

text = open(path).read()
newtext = ""
for character in text:
    if '\t' == character:
        newtext+=" "*4
    else:
        newtext+=character

open(path, 'w').write(newtext)
