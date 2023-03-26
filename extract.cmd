sed -r 's/[^0-9]*([0-9]+)[^0-9]*/\1 /g; s/ $//; /^$/d' filename.txt

