#!/bin/bash

dir_path="$1"
num_of_recent="$2"
output_file_path="$3"

# Getting the names of the 10 most recent .log files
log_files=$(ls -t "$dir_path"*.log | head -n "$num_of_recent")

# Creating the output file
> "$3"

# Loop through each log file and get the first line
for file in $log_files; do
  head -n 1 "$file" >> "$3"
done
