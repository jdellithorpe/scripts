#!/bin/bash
#
# ./FilePartitioner.sh <file> <linesperpartition>
# 
# A convenience script for partitioning files.  This script will preserve the
# first line (header) of the original file in each of the partitions. 

file=$1
lines=$2
export file
split_filter () { { head -n 1 $file; cat; } > "$FILE"; }
export -f split_filter
tail -n +2 $file | split --lines=$lines --filter=split_filter -d --suffix-length=4 - ${file}.part
