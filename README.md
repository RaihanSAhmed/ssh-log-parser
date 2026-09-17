SSH Log Parser & Security Event Normalizer

A beginner-friendly Python automation script designed to parse raw, unstructured Linux SSH authentication logs and normalize them into structured JSON data. Built as part of a security engineering and detection portfolio.

🚀 Project Overview

In a security engineering role, dealing with raw log data is a daily reality. Syslog data is unstructured text, making it difficult for automated tools and analytics platforms to query effectively.

This project solves that problem by building a lightweight Python script that filters background noise, extracts key indicators of compromise (IOCs) or failed login attempts, and formats them into clean JSON.

🛠️ Tech Stack

Language: Python 3

Environment: Windows Command Prompt (CMD)

Data Format: JSON

📂 Project Structure

ssh-log-parser/
│
├── logs/
│   └── sample_auth.log      # Raw input authentication logs
├── parser.py                # Python automation script
├── output.json              # Cleaned, structured security events
└── README.md                # Project documentation


🔍 How It Works (parser.py)

Line-by-Line Ingestion: The script reads the raw log file iteratively to ensure high memory efficiency.

Noise Filtering: It checks for the string "Failed password" to isolate unauthorized access attempts from normal system background tasks.

Data Normalization: It chops the log line into an array of words using .split() and extracts crucial fields:

Timestamp (Month, Day, Time)

Event Type (Failed SSH Login)

Target User (Dynamic extraction handling standard and invalid users)

Source IP (The origin address of the attack attempt)

Structured Export: Packages the extracted dictionary data and writes it cleanly to output.json with indentation.

💻 How to Run It Locally

Clone or download this repository.

Ensure you have Python installed.

Open your terminal inside the project directory and run:

python parser.py


View the structured output:

type output.json


📸 Sample Output (output.json)

[
    {
        "timestamp": "Sep 17 04:15:22",
        "event": "Failed SSH Login",
        "user": "admin",
        "source_ip": "192.168.1.50"
    }
]


🎯 Key Takeaways & Portfolio Value

Demonstrated proficiency in text manipulation, string parsing, and file I/O in Python.

Built a foundational telemetry-normalization pipeline mimicking basic SIEM (Security Information and Event Management) preprocessing workflows.
