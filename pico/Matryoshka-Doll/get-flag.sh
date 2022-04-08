#!/bin/sh

# Run the initial binwalk extraction on the given file.
binwalk -e dolls.jpg > /dev/null
cd _dolls.jpg.extracted/base_images

for i in $(seq 2 5); do
    filename=${i}_c.jpg
    binwalk -e ${filename} > /dev/null 2>&1
    cd _${filename}.extracted/base_images > /dev/null 2>&1
done;

flag_file_path=$(find | grep 'flag')

cat $flag_file_path
echo
