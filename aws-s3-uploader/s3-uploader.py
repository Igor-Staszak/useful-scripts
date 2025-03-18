import sys
import boto3
from pathlib import Path

def upload_files(bucket_name, files):
    s3 = boto3.client('s3')
    for file in files:
        if not Path(file).is_file():
            print(f"ERROR: File '{file}' does not exist or is not a regular file.")
            return
        try:
            s3.upload_file(file, bucket_name, file)
            print(f"INFO: Successfully uploaded {file} to {bucket_name}")
        except Exception as e:
            print(f"ERROR: Failed to upload {file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: <bucket> <file1> <file2> ...")
        sys.exit(1)
    bucket_name = sys.argv[1]
    files = sys.argv[2:]
    upload_files(bucket_name, files)
