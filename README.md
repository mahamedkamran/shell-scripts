# System Health Monitor

## Description
The **System Health Monitor** is a Bash script designed to monitor the health of a Linux system. It checks key metrics such as CPU usage, memory usage, disk space, and the number of running processes. If any metric exceeds predefined thresholds, the script logs an alert to the console and a specified log file.

## Features
- Monitors:
  - **CPU Usage**
  - **Memory Usage**
  - **Disk Space**
  - **Running Processes**
- Logs alerts with timestamps.
- Configurable thresholds.
- Lightweight and easy to use.

## Prerequisites
Ensure the following tools are installed and available on your system:
- `bash`
- `top`
- `free`
- `df`
- `awk`
- `ps`
- `tee`

## Configuration
You can configure the thresholds and log file path by editing the script:

```bash
# Configuration: thresholds and log file
CPU_THRESHOLD=80
MEMORY_THRESHOLD=80
DISK_THRESHOLD=90
PROCESS_THRESHOLD=200
LOG_FILE="/var/log/system_health_monitor.log"
```

- **CPU_THRESHOLD**: Maximum allowed CPU usage (%)
- **MEMORY_THRESHOLD**: Maximum allowed memory usage (%)
- **DISK_THRESHOLD**: Maximum allowed disk space usage (%)
- **PROCESS_THRESHOLD**: Maximum allowed number of running processes
- **LOG_FILE**: Path to the log file

## Usage

### Run the Script
1. Save the script to a file, e.g., `system_health_monitor.sh`.
2. Make the script executable:
   ```bash
   chmod +x system_health_monitor.sh
   ```
3. Run the script manually:
   ```bash
   ./system_health_monitor.sh
   ```

### Automate with Cron
To automate system health monitoring, schedule the script using `cron`. For example, to run it every 5 minutes:

1. Open the crontab editor:
   ```bash
   crontab -e
   ```
2. Add the following line:
   ```bash
   */5 * * * * /path/to/system_health_monitor.sh
   ```

### Log File
Alerts are logged in the specified log file (`/var/log/system_health_monitor.log` by default). Ensure the script has write permissions for the log file location.

## Output Example
Here is an example of a log entry:

```plaintext
Tue Dec 24 18:25:51 UTC 2024: ALERT: CPU usage is at 85% (threshold: 80%)
Tue Dec 24 18:25:51 UTC 2024: ALERT: Memory usage is at 90% (threshold: 80%)
Tue Dec 24 18:25:51 UTC 2024: ALERT: Disk usage on /home is at 95% (threshold: 90%)
Tue Dec 24 18:25:51 UTC 2024: ALERT: Number of running processes is 250 (threshold: 200)
```

## Troubleshooting

1. **Script Fails to Run:**
   Ensure you are running the script with `bash`:
   ```bash
   bash system_health_monitor.sh
   ```

2. **Permissions Error:**
   If the script cannot write to the log file, adjust the permissions:
   ```bash
   sudo chmod 666 /var/log/system_health_monitor.log
   ```

3. **Command Not Found:**
   Verify that required tools (`top`, `free`, etc.) are installed and available in your system's `PATH`.

# Backup Script

## Description

This script provides a simple and efficient solution for securely backing up a local file to a remote server using SFTP. The script leverages the `paramiko` library to establish an SSH connection, ensures the destination directory exists, and transfers the file while logging all operations.

## Features

- Transfers a specified local file to a remote server directory using SFTP.
- Automatically creates the remote directory if it doesn't exist.
- Maintains a log of all operations with timestamps for auditing and troubleshooting.

## Prerequisites

1. **Python**: Ensure Python 3.x is installed on your system.
2. **Paramiko Library**: Install the `paramiko` library using pip:
   ```bash
   pip install paramiko
