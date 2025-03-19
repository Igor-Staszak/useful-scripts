# Server Resource Monitor Script

Bash script responsible for monitoring disk and memory usage on a Linux server. Logs usage statistics, send system alerts using `logger` and emails an administrator if usage exceeds predefined thresholds.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation and setup](#installation-and-setup)
  - [Prepare the script and its configuration](#prepare-the-script-and-its-configuration)

## Features

- logs disk and memory usage every execution
- alerts system logs (`journalctl`) if disk or memory usage exceeds thresholds
- sends an email notification if a threshold is crossed
- designed to run every 5 minutes via `cron`

## Prerequisites

- `mail` installed for email notifications (`mailutils` on Debian/Ubuntu, `mailx` on RHEL/CentOS)

## Installation and setup

The script is designed to be run evey X minutes using `cron`.

### Prepare the script and its configuration

1. Configure the script:
   - Replace the `EMAIL=""` with a valid administrator email.
   - Adjust `DISK_THRESHOLD` and `MEM_THRESHOLD` if needed.
   - Set the `LOG_FILE` path.
2. Make the script executable
    ```bash
    chmod +x /path/to/disk_memory_alert.sh 
    ```
3. Schedule using `cron` (in this case every 5 minutes).
   - Edit the crontab:
    ```bash
    crontab -e
    ```
   - Add the following line (if needed, change the cron expression):
   ```bash
   */5 * * * * /path/to/disk_memory_alert.sh
   ```
4. Verify execution:
   - Check the log file:
    ```bash
    tail -f /var/log/resource_monitor.log
    ```
   - Check system logs:
    ```bash
    journalctl -p warning -n 20
    ```

