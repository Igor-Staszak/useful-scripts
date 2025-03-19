#!/bin/bash

LOG_FILE="/var/log/resource_monitor.log"
DISK_THRESHOLD=90
MEM_THRESHOLD=90
EMAIL=""
HOSTNAME=$(cat /etc/hostname)

DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
MEM_USAGE=$(free | awk '/Mem/ {printf "%.0f", $3/$2 * 100}')
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

echo "$TIMESTAMP - Disk usage: $DISK_USAGE%; memory usage: $MEM_USAGE%." > $LOG_FILE

if [ "$DISK_USAGE" -gt "$DISK_THRESHOLD" ]; then
  logger -p syslog.warning "Disk usage alert: $DISK_USAGE% used!"
fi

if [ "$MEM_USAGE" -gt "$MEM_THRESHOLD" ]; then
  logger -p syslog.warning "Memory usage alert: $MEM_USAGE% used!"
fi

if [ "$DISK_USAGE" -gt "$DISK_THRESHOLD" ] || [ "$MEM_USAGE" -gt "$MEM_THRESHOLD" ]; then
    echo -e "$TIMESTAMP - Server Resource Alert:\nDisk Usage: $DISK_USAGE%\nMemory Usage: $MEM_USAGE%" | mail -s "$HOSTNAME - server resource alert" "$EMAIL"
fi
