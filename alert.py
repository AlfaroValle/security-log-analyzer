def classify_alert(failed_ips):
    alerts = []

    for ip, count in failed_ips.items():
        if count >= 3:
            severity = "HIGH"
        elif count == 2:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        alerts.append(f"{severity}: {ip} had {count} failed attempts")

    return alerts
