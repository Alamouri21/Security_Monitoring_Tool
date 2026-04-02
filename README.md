 Security Monitoring Toolkit

A lightweight, modular Python toolkit for real-time system security monitoring. Available in both a **Command-Line (CLI)** and **Graphical (GUI)** interface, it provides five core security tools that help you monitor your system, analyze login activity, detect suspicious processes, and scan log files.

---

#  Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [CLI Version](#cli-version)
  - [GUI Version](#gui-version)
- [Modules](#modules)
- [Sample Log Files](#sample-log-files)
- [Screenshots](#screenshots)
- [License](#license)

---

## ✨ Features

| Tool | Description |
|------|-------------|
|  OS Fingerprinting | Displays OS name, version, machine type, processor, and node info |
|  Log File Scanner | Scans the current directory for `.log` files and reports their sizes |
|  Suspicious Process Detector | Lists running processes and flags those running under ADMIN privileges |
|  Network Monitor | Shows active network connections and all listening ports |
|  Login Activity Analyzer | Parses login log files to report successful/failed login attempts per IP |

---

##  Project Structure

```
security-toolkit/
│
├── Command-Line_Menu_Version.py   # CLI entry point
├── GUI_Version.py                 # GUI entry point (Tkinter)
│
├── os_fingerprinting.py           # OS info module
├── log_file_scanner.py            # Log file size scanner
├── suspicious_process_detector.py # Process privilege checker
├── network_monitor.py             # Network connections monitor
├── login_activity_analyzer.py     # Login log parser & analyzer
│
├── login.log                      # Sample login log (single-timestamp)
├── login_log.txt                  # Sample login log (timestamped entries)
├── t1_log.txt                     # Sample server activity log
├── t2_log.txt                     # Additional test log
└── test_log.txt                   # Test log file
```

---

##  Requirements

- Python 3.7+
- [`psutil`](https://pypi.org/project/psutil/) — for process and network monitoring
- `tkinter` — for the GUI version (included with most Python installations)

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/security-toolkit.git
cd security-toolkit
```

2. **Install dependencies:**

```bash
pip install psutil
```

> `tkinter` is bundled with standard Python. If it's missing, install it via your OS package manager (e.g., `sudo apt install python3-tk` on Debian/Ubuntu).

---

##  Usage

### CLI Version

Run the command-line menu interface:

```bash
python "Command-Line_Menu_Version.py"
```

You will see an interactive menu:

```
=== Security Monitoring Toolkit ===
1. OS Fingerprinting
2. File Scanner for Security Logs
3. Suspicious Process Detector
4. Network Connection Monitor
5. Login Activity Analyzer
0. Exit

Enter your choice:
```

Type a number and press Enter to run the corresponding tool.

---

### GUI Version

Launch the graphical interface:

```bash
python "GUI_Version.py"
```

A dark-themed window will open with sidebar buttons for each tool. Output is displayed in a scrollable terminal area. Use the **Clear Terminal** button to reset the output panel.

---

## 🔧 Modules

### `os_fingerprinting.py`
Uses Python's `platform` library to display:
- OS Name & Version
- Machine architecture
- Processor type
- Release & Node name

### `log_file_scanner.py`
Scans the current working directory for `.log` files and reports:
- File name
- File size (in MB)
- Size label: `SMALL` (< 1 MB) or `LARGE` (≥ 1 MB)

### `suspicious_process_detector.py`
Iterates over all running processes using `psutil` and labels each as:
- `ADMIN` — if running under `root` or `Administrator`
- `USER` — all other processes

### `network_monitor.py`
Uses `psutil` to display:
- All active network connections (local/remote address and status)
- All ports currently in `LISTEN` state with their associated PID

### `login_activity_analyzer.py`
Parses a `.log` file and reports:
- Total login attempts per IP address
- Number of successful vs. failed attempts
- IPs with repeated failures (potential brute-force indicators)

**Expected log format:**
```
2026-03-17 09:30:01 - INFO - User login successful from IP 192.168.1.1
2026-03-17 09:32:15 - INFO - User login failed from IP 192.168.1.2
```

---

 Sample Log Files

| File | Description |
|------|-------------|
| `login.log` | Compact login events, multiple IPs, same-second timestamps |
| `login_log.txt` | Spread-out login events with realistic timestamps |
| `t1_log.txt` | Full server log: INFO, WARNING, ERROR, DEBUG events |
| `t2_log.txt` | Additional test log data |
| `test_log.txt` | General-purpose test log |
