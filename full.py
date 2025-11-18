import random
import logging

# Configure logging system
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# List of cybersecurity incidents with severity levels
incidents = {
    "Phishing Attack": 2,
    "Malware Infection": 3,
    "Unauthorized Access": 4,
    "Ransomware Attack": 5
}

# Randomly detect an incident
detected_incident = random.choice(list(incidents.keys()))
severity = incidents[detected_incident]

# Log detected incident
logging.info(f"Detected Incident: {detected_incident} (Severity: {severity})")

# Decision-making based on severity
if severity == 5:
    print("\n⚠️ CRITICAL ALERT: Ransomware Detected!")
    print("→ Isolating affected systems immediately...")
    print("→ Blocking network traffic...")
    print("→ Initiating rapid containment measures...\n")
    logging.warning("Immediate containment executed due to ransomware.")

elif severity >= 4:
    print("\n🔐 High-Severity Incident Detected:", detected_incident)
    print("→ Starting containment and forensic analysis...\n")
    logging.warning("High severity incident. Containment procedures initiated.")

elif severity >= 3:
    print("\n🛡️ Medium-Severity Incident:", detected_incident)
    print("→ Quarantining affected files and scanning system...\n")
    logging.info("Medium severity actions taken.")

else:
    print("\n📨 Low-Severity Incident:", detected_incident)
    print("→ Verifying user report and checking logs...\n")
    logging.info("Low severity incident logged and analyzed.")

# Final step
print("✔ Incident Response Step Completed.")
logging.info("Incident response workflow completed.\n")
