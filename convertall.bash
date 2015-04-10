#!/bin/bash
for file in *.pdf
do  
    echo "$file"
    convert -density 100 "$file" -quality 90 "${file%.pdf}.png"
done
