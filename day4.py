def log_analyzer_fast(logs):
    counts = {"ERROR": 0, "INFO": 0, "WARNING": 0}

    for log in logs:
        log_type = log.upper().split()[0]   # Extract first word
        if log_type in counts:
            counts[log_type] += 1

    most_frequent = max(counts, key=counts.get)
    return counts, most_frequent


# Example usage
logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

counts, most_frequent = log_analyzer_fast(logs)
print("Counts:", counts)
print("Most Frequent:", most_frequent)