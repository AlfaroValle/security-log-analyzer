# Automated Security Log Analysis and Alert System

## Project Overview
This project is a Python-based security automation tool designed to analyze system and network log files to detect potential security threats. It automates the process of identifying suspicious activity such as repeated failed login attempts and unusual IP behavior.

The goal is to improve efficiency in cybersecurity workflows by reducing manual log analysis and enabling faster incident response.

---

## Objectives
- Automate log file analysis using Python  
- Detect indicators of compromise (IOCs)  
- Classify alerts based on severity levels  
- Generate structured alert outputs  
- Demonstrate security automation concepts  

---

## Features
- Log file parsing and analysis  
- Pattern matching using regular expressions  
- Detection of failed login attempts  
- Severity-based alert classification (Low, Medium, High)  
- Output results to console and file  

---

## Project Structure

security-log-analyzer/
│── logs/ # Sample log files
│── src/ # Source code
│ ├── main.py
│ ├── parser.py
│ ├── detector.py
│ └── alert.py
│── reports/ # Output reports
│── README.md


---

## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/security-log-analyzer.git
cd security-log-analyzer

Run the Program
cd src
python main.py

Run the program
HIGH: 192.168.1.10 had 3 failed attempts
LOW: 10.0.0.3 had 1 failed attempts

Requirements
Python 3.x
No external libraries required

Use of AI Tools

AI tools such as ChatGPT were used to assist with:

Designing the project structure
Writing and improving Python code
Debugging and refining logic

All code was reviewed and modified to ensure full understanding.

Ethical Considerations

This project is intended for educational purposes only. It should only be used on systems where you have proper authorization.

Project Status

Completed as a working prototype for security log analysis and alert generation.

Author

Brandon Alfaro Valle

## 🔹 Step 4: Replace Your GitHub Username

Find this line:

```bash
git clone https://github.com/AlfaroValle/security-log-analyzer.git 

Step 5: Save the File

Press:

Ctrl + S   (Windows)
Cmd + S    (Mac)

Step 6: Push README to GitHub

In VS Code terminal:

git add README.md
git commit -m "Added README"
git push

Step 7: Check It on GitHub
Go to your GitHub repo
Refresh the page
You should now see your README displayed nicely
