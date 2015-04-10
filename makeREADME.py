#!/usr/bin/python -tt

listpng = open("listpng.txt", "r")
data = listpng.readlines()

print """# Tikz by Example
drawing in tikz or pgf
"""
for name in data:
    print name,"!["+name[0:-5]+"](https://raw.githubusercontent.com/ridlo/tikz_by_example/master/"+name+")\n"

