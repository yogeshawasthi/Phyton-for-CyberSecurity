import logging
import random

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Step 1: Preparation Logs
logging.info("Incident Response Plan initiated.")
logging.info("Formed Incident Response Team (IRT).")
logging.info("Deployed SIEM and EDR tools.")
logging.info("Conducted staff training on incident response.")

# Step 2: Detect Incident
incidents = ["Phishing Attack", "Malware Infection", "Unauthorized Access", "Ransomware Attack"]
detected = random.choice(incidents)
print(f"\nDetected Incident: {detected}")

# Step 3: Take Action
def isolate_system(ip):
    print(f"Isolating system {ip}... Network traffic blocked.")

def remove_malware():
    print("Scanning system... Malware removed.")

# Incident Handling Logic
if detected == "Ransomware Attack":
    print("⚠️ Ransomware detected! Starting immediate containment.")
    isolate_system("192.168.1.101")
else:
    print("Analyzing further...")
    if detected == "Malware Infection":
        remove_malware()
