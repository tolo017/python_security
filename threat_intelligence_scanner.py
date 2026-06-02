# DAY 4: Our threat intelligence database (Dictionary)
known_threats = {
    "192.168.1.99": "Malware Server",
    "10.0.0.42": "Data Thief",
    "172.16.0.5": "Spam Bot"
}

# DAY  3: Our reusable tool (Function)
def analyze_logs(file_name):
    print("Opening secure vault...")
    
    # DAY 4: Opening the external file
    with open(file_name, 'r') as file:
        # We read the file and split the text into a List of separate lines.
        log_entries = file.read().splitlines()
        
        # DAY 2: Looping through the external data
        for ip in log_entries:
            
            # DAY 1 & 4 combined: If the IP is a Key in our Dictionary...
            if ip in known_threats:
                
                # We pull the specific Value (Threat Type) from the Dictionary
                threat_type = known_threats[ip]
                print("CRITICAL ALERT: Connection from " + ip + " - " + threat_type)
            else:
                print("Connection from " + ip + " is safe.")
                
# Run the tool on our external file!
analyze_logs("traffic_logs.txt")