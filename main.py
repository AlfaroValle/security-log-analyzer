from parser import parse_logs
from detector import detect_failed_logins
from alert import classify_alert

logs = parse_logs("../sample.log")
failed_ips = detect_failed_logins(logs)
alerts = classify_alert(failed_ips)

# Print results
for alert in alerts:
    print(alert)

# Save to file
with open("reports/output.txt", "w") as f:
    for alert in alerts:
        f.write(alert + "\n")
