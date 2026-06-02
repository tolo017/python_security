# The "r" stands for "read". We are just reading the file, not changing it.
with open("server_logs.txt", "r") as file:
    historical_data = file.read()
    
    print("Log file success opened. Data loaded.")