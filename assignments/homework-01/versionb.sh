#!/bin/bash
old=$1
name=${old%.*}
extension=${old##*.}
cp $old "$name"_$(date --rfc-3339=date).$extension