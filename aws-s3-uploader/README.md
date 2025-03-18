# AWS S3 File Uploader

This repository contains two scripts for uploading files to an Amazon S3 bucket:
- A **Python script** using the `boto3` library.
- A **Bash script** using the AWS CLI.

## Table of Contents

- [Usage](#usage)
  - [Python Script](#python-script)
  - [Bash Script](#bash-script)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Option 1: Add to `.bashrc` (Alias)](#option-1-add-to-bashrc-alias)
  - [Option 2: Add to `bin` Directory](#option-2-add-to-bin-directory)

---

## Usage

### Python Script

Run the Python script with the following syntax:

```bash
python3 s3-uploader.py <bucket> <file1> <file2> ...
```

You must provide the bucket name and at least one file name.\
Example:

```bash
python3 s3-uploader.py my-bucket file1.txt file2.jpg
```

### Bash Script

Run the Bash script with the following syntax:

```bash
./s3-uploader.sh <bucket> <file1> <file2> ...
```

You must provide the bucket name and at least one file name.\
Example:

```bash
./s3-uploader.sh my-bucket file1.txt file2.jpg
```

---

## Prerequisites

### Both scripts
- AWS CLI installed.
- AWS credentials configured.

### Python script (additional)
- Python 3 installed.
- `boto3` library installed.

---

## Installation

### Option 1: Add to `.bashrc` (Alias)

To run the script from anywhere, add an alias in your `.bashrc` or `.bash_profile`:

For the **Python script**:
```bash
alias s3_upload_py="python3 /path/to/s3-uploader.py"
```

For the **Bash script**:
```bash
alias s3_upload_sh="/path/to/s3-uploader.sh"
```

Reload the shell configuration:
```bash
source ~/.bashrc
```

Now, you can use:
```bash
s3_upload_py my-bucket file.txt
s3_upload_sh my-bucket file.txt
```

### Option 2: Add to `bin` Directory

1. Move the script to a directory in your `PATH` (e.g., `/usr/local/bin`):

   ```bash
   mv s3-uploader.py /usr/local/bin/s3-uploader-py
   mv s3-uploader.sh /usr/local/bin/s3-uploader-sh
   ```

2. Make them executable (only required for the Bash script):

   ```bash
   chmod +x /usr/local/bin/s3-uploader-sh
   ```

Now, you can simply run:

```bash
s3-uploader-py my-bucket file.txt  # Python version
s3-uploader-sh my-bucket file.txt  # Bash version
```
