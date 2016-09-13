#!/bin/bash
#words=$(more /usr/share/dict/words)
c=0
while read line
do
  words[$c]=$line
  ((c+=1))
done < /usr/share/dict/words
echo "Your random word is" ${words[$RANDOM % ${#words[@]}]}