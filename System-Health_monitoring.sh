#!/bin/sh

CPU_THRESHOLD=80
MEMORY_THRESHOLD=80
DISK_THRESHOLD=90
PROCESS_THRESHOLD=200
LOG_FILE="/var/log/system_health_monitor.log"

log_message() {
  echo "$(date): $1" >> "$LOG_FILE"
}

check_cpu_usage() {
  cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
  cpu_usage=${cpu_usage%.*}
  if [ "$cpu_usage" -gt "$CPU_THRESHOLD" ]; then
    log_message "ALERT: CPU usage is at ${cpu_usage}% (threshold: ${CPU_THRESHOLD}%)"
  fi
}

check_memory_usage() {
  memory_usage=$(free | awk '/Mem/ {printf("%.0f", $3/$2 * 100)}')
  if [ "$memory_usage" -gt "$MEMORY_THRESHOLD" ]; then
    log_message "ALERT: Memory usage is at ${memory_usage}% (threshold: ${MEMORY_THRESHOLD}%)"
  fi
}

check_disk_usage() {
  df -h | awk 'NR>1 {print $5, $6}' | sed 's/%//' | while read usage mount; do
    if [ "$usage" -gt "$DISK_THRESHOLD" ]; then
      log_message "ALERT: Disk usage on $mount is at ${usage}% (threshold: ${DISK_THRESHOLD}%)"
    fi
  done
}

check_running_processes() {
  process_count=$(ps aux | wc -l)
  if [ "$process_count" -gt "$PROCESS_THRESHOLD" ]; then
    log_message "ALERT: Number of running processes is ${process_count} (threshold: ${PROCESS_THRESHOLD})"
  fi
}

monitor_system() {
  log_message "Starting system health check"
  check_cpu_usage
  check_memory_usage
  check_disk_usage
  check_running_processes
  log_message "System health check completed"
}

monitor_system
