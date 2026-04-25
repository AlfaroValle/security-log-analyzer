import re

def detect_failed_logins(logs):
    pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"
    failed_ips = {}

    for line in logs:
        match = re.search(pattern, line)
        if match:
            ip = match.group(1)
            failed_ips[ip] = failed_ips.get(ip, 0) + 1

    return failed_ips
