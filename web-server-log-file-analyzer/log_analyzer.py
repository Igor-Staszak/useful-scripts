import re
import sys
from collections import Counter

LOG_FILE = ""

LOG_PATTERN = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.*?)\] '
    r'"(?P<method>GET|POST|PUT|DELETE) (?P<url>\S+) HTTP/1.\d" '
    r'(?P<status>\d{3}) (?P<response_size>\d+) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"'
)


def analyze_log():
    try:
        with open(LOG_FILE, "r") as file:
            log_lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: {LOG_FILE} not found.")
        sys.exit(1)

    status_counter = Counter()

    for line in log_lines:
        match = LOG_PATTERN.match(line)
        if match:
            status = match.group("status")
            status_counter[status] += 1

    print("=== Log Analysis Report ===")
    print("Status Code Summary:")
    for status, count in status_counter.most_common():
        print(f"  {status}: {count} requests")


if __name__ == "__main__":
    analyze_log()
