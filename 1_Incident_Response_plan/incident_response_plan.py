import logging   # Import Python's built-in logging module

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,                      # Set logging level to INFO (shows INFO and above)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Format: time - level - message
)

# Log preparation activities
logging.info("Incident Response Plan initiated.")  
# Logs that the incident response plan has started

logging.info("Formed Incident Response Team (IRT).")
# Logs that the incident response team has been created

logging.info("Deployed SIEM and EDR tools.")
# Logs that security tools (SIEM & EDR) have been deployed

logging.info("Conducted staff training on incident response procedures.")
# Logs that staff members were trained for incident response
