# Web server Log Analyzer

The script analyzes a web serveer access log (Apache/Nginx) and provides a summary of HTTP status codes. It helps monitor server traffic, detect errors and troubleshoot issues.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
  - [Example output](#example-output)
- [Potential improvements](#potential-improvements)

## Features

- Parses logs and extracts HTTP status codes
- Counts occurrences of each status code
- Works with standard Apache/Nginx log formats
- Simple and lightweight

## Usage

1. Set the log file variable:
   ```bash
   LOG_FILE = "/var/log/nginx/access.log" # Example path
   ```
2. Run the script:
   ```bash
   python3 log_analyzer.py
   ```

### Example output:

For the sample `access_log_apache.log` file:
```bash
=== Log Analysis Report ===
Status Code Summary:
  200: 877 requests
  301: 53 requests
  404: 17 requests
  206: 17 requests
```

For the sample `access_log_nginx.log` file:
```bash
=== Log Analysis Report ===
Status Code Summary:
  404: 688 requests
  304: 274 requests
  200: 21 requests
  206: 1 requests
```

## Potential improvements

- The script can be modified to analyze request methods, user agents, response times.
- If needed, the regular expressions should be adjusted to match the log format used in your web server logs.
