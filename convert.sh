#!/bin/bash

input_dir="datasets"
output_dir="datasets/wav"

mkdir -p "$output_dir"

for input_file in "$input_dir"/*.mp3; do
    filename=$(basename "$input_file" .mp3)
    output_file="$output_dir/$filename.wav"
    ffmpeg -i "$input_file" -ar 16000 -ac 1 -c:a pcm_s16le "$output_file"
    echo "Converted $input_file to $output_file"
done
