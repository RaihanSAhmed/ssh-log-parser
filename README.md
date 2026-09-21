# SSH Log Parser & Security Event Normalizer

A Python automation script that parses raw Linux SSH authentication logs, extracts failed login events, and converts them into structured JSON data.

## Project Overview

Linux SSH authentication logs contain useful security information, but the raw format is unstructured text. This makes the data harder to analyze programmatically.

This project automates the initial parsing process by:

- Reading SSH authentication logs line by line
- Identifying failed password attempts
- Extracting timestamps, usernames, and source IP addresses
- Converting the events into structured JSON

The resulting data can be used as a starting point for further security analysis or SIEM ingestion.

## Tech Stack

- **Language:** Python 3
- **Data Format:** JSON
- **Environment:** Windows Command Prompt (CMD)

## Project Structure

```text
ssh-log-parser/
│
├── logs/
│   └── sample_auth.log   # Sample SSH authentication logs
├── parser.py             # Python log parsing script
├── output.json           # Structured security events
└── README.md             # Project documentation
