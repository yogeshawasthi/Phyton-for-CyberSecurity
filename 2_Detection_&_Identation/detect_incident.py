import random  # Import random module to select random incidents

# List of possible incidents
incidents = ["Phishing Attack", "Malware Infection", "Unauthorized Access", "Ransomware Attack"]

# Randomly select one incident to simulate detection
detected_incident = random.choice(incidents)

# Print the detected incident
print(f"Detected Incident: {detected_incident}")

# Check if the detected incident is ransomware
if detected_incident == "Ransomware Attack":
    # If ransomware is detected, initiate urgent containment
    print("Initiating immediate containment procedures.")
else:
    # For other incidents, analyze further
    print("Analyzing further to confirm incident type.")
