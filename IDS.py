# 1. MODULES (Day 5)
import time

# 2. DICTIONARIES (Day 4): Our authorized user database
admin_database = {
    "admin_alpha": "Main Cloud Sever",
    "admin_beta": "Solar Backup Node",
}

# 3. FUNCTIONS (Day 3): Packaging our tool
def monitor_soc_dashboard(log_file):
    print("Initiating SOC Dashboard Monitor...")
    time.sleep(1)  # Dramatic pause
    
    # 4. ERROR HANDLING (Day 5)
    try:
        # 5. FILE HANDLING (Day 4): Reading the log file
        with open(log_file, "r") as file:
            # Turns the file into a LIST (Day 2)
            access_attempts = file.read().splitlines()
            
            # 6. LOOPS (Day 2): Processing each access attempt
            for user in access_attempts:
                time.sleep(1) # Slow it down so we can read the output
                
                # 7. LOGIC (Day 1): Check if the user is in our dictionary
                if user in admin_database:
                    # They are safe!
                    server_name = admin_database[user]
                    print("ACCESS GRANTED: " + user + " connected to " + server_name)
                else:
                    # They are an intruder!
                    print("SOC ALERT: Unauthorized access blocked for -> " + user)
                    
    except FileNotFoundError:
        print("SYSTEM ERROR: Log file is missing. The server might be completely offline.")
        
# 8. RUN THE TOOL
# (To run this for real, just create a text file named 'server_logs.txt' with names like 'admin_alpha', 'admin_beta', and 'hacker_99' on separate lines!)
monitor_soc_dashboard("server_logs.txt")