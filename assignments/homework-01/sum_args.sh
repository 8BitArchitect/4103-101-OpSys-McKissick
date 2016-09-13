#!/bin/bash
sum=0
for arg in $@
do
	((sum+=arg))
done
echo $sum