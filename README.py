#!/usr/bin/python -tt
import glob

ifile = open("README.md", 'w')
header = """# Tikz by Example
drawing in tikz or pgf

"""
ifile.write(header)

data = glob.glob("*.png")
for name in data:
    ifile.write(name[0:-4]+"\n!["+name[0:-4]+"](https://raw.githubusercontent.com/ridlo/tikz_by_example/master/"+name+")\n\n")
