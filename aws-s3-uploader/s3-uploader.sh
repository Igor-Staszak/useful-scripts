#!/bin/bash

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <bucket> <file1> <file2> ..."
  exit 1
fi

bucket=$1
shift

for file in "$@"; do
  if [ ! -f "$file" ]; then
    echo "ERROR: File '$file' does not exist or is not a regular file."
    exit 1
  fi

  if aws s3 cp "$file" "s3://$bucket/"; then
    echo "INFO: Successfully uploaded $file to $bucket"
  else
    echo "ERROR: Failed to upload $file"
    exit 1
  fi
done
