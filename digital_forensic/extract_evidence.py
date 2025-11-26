log_data = [
    "2024-11-19 10:00:00 - INFO - Phishing email detected.",
    "2024-11-19 10:05:00 - WARNING - User clicked on phishing link.",
    "2024-11-19 10:10:00 - CRITICAL - Unauthorized access detected."
]

print("Extracted Evidence:")

for log in log_data:
    if "CRITICAL" in log or "WARNING" in log:
        print(log)

    else:
        print("further operations should be done in advance to complete")    
        print("No more worries")
