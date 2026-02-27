def detect_bruteforce(logs):
    suspicious = []
    ip_counts = {}

    for log in logs:
        if "failed login" in log.message.lower():
            ip_counts[log.source_ip] = ip_counts.get(log.source_ip, 0) + 1

    for ip, count in ip_counts.items():
        if count >= 5:
            suspicious.append(f"Brute force suspected from {ip}")

    return suspicious
