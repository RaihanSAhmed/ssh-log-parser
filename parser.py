import json

# 1. Define where our input log file is and where our output JSON will go
log_file_path = "logs\\sample_auth.log"
output_file_path = "output.json"

# 2. Create an empty list to store the security events we successfully extract
parsed_logs = []

# 3. Open and read the log file line by line
with open(log_file_path, "r") as file:
    for line in file:
        # Look only for lines that contain a failed password attempt
        if "Failed password" in line:
            
            # Chop the sentence into a list of individual words based on spaces
            words = line.split()
            
            # Grab the month, day, and time (words at positions 0, 1, and 2)
            timestamp = f"{words[0]} {words[1]} {words[2]}"
            
            # Find the target username and the source IP address
            if "invalid user" in line:
                user = words[words.index("user") + 1]
            else:
                user = words[words.index("for") + 1]
                
            ip = words[words.index("from") + 1]
            
            # Package it neatly into a dictionary (like a mini profile for the event)
            log_entry = {
                "timestamp": timestamp,
                "event": "Failed SSH Login",
                "user": user,
                "source_ip": ip
            }
            
            # Add it to our list of parsed logs
            parsed_logs.append(log_entry)

# 4. Save our clean list into a structured JSON file
with open(output_file_path, "w") as outfile:
    json.dump(parsed_logs, outfile, indent=4)

print(f"[+] Success! Parsed {len(parsed_logs)} events and saved to {output_file_path}")