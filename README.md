[project_readme.md](https://github.com/user-attachments/files/32359079/project_readme.md)
SSH Log Parser & Security Event Normalizer
A beginner-friendly Python automation script designed to parse raw, unstructured Linux SSH authentication logs and normalize them into structured JSON data. Built as part of a security engineering and detection portfolio.

## 🚀 Project Overview

In a security engineering role, dealing with raw log data is a daily reality. Syslog data is unstructured text, making it difficult for automated tools and analytics platforms to query effectively.

This project solves that problem by building a lightweight Python script that filters background noise, extracts key indicators of compromise (IOCs) or failed login attempts, and formats them into clean JSON.

## 🛠️ Tech Stack

* **Language:** Python 3
* **Environment:** Windows Command Prompt (CMD)
* **Data Format:** JSON

## 📂 Project Structure

```text
ssh-log-parser/
│
├── logs/
│   └── sample_auth.log   # Raw input authentication logs
├── parser.py             # Python automation script
├── output.json           # Cleaned, structured security events
└── README.md             # Project documentation
```

## 🔍 How It Works (`parser.py`)

1. **Line-by-Line Ingestion:** The script reads the raw log file iteratively to ensure high memory efficiency.
2. **Noise Filtering:** It checks for the string `"Failed password"` to isolate unauthorized access attempts from normal system background tasks.
3. **Data Normalization:** It chops the log line into an array of words using `.split()` and extracts crucial fields:
   * **Timestamp:** Month, Day, Time
   * **Event Type:** Failed SSH Login
   * **Target User:** Dynamic extraction handling standard and invalid users
   * **Source IP:** The origin address of the attack attempt
4. **Structured Export:** Packages the extracted dictionary data and writes it cleanly to `output.json` with indentation.

## 💻 How to Run It Locally

1. Clone or download this repository.
2. Ensure you have Python installed.
3. Open your terminal inside the project directory and run:
   ```cmd
   python parser.py
   ```
4. View the structured output:
   ```cmd
   type output.json
   ```

## 📸 Sample Output (`output.json`)

```json
[
    {
        "timestamp": "Sep 17 04:15:22",
        "event": "Failed SSH Login",
        "user": "admin",
        "source_ip": "192.168.1.50"
    }
]
```

## 🎯 Key Takeaways & Portfolio Value

* Demonstrated proficiency in text manipulation, string parsing, and file I/O in Python.
* Built a foundational telemetry-normalization pipeline mimicking basic SIEM (Security Information and Event Management) preprocessing workflows.
