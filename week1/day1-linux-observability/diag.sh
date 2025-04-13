#!/bin/bash
echo "===== UPTIME ====="
uptime

echo -e "\n===== TOP CPU PROCESSES ====="
ps aux --sort=-%cpu | head -n 5

echo -e "\n===== MEMORY USAGE ====="
free -h

echo -e "\n===== I/O Activity ====="
iostat -xz 1 3

echo -e "\n===== OPEN TCP PORTS ====="
ss -tuln

echo -e "\n===== DISK USAGE ====="
df -h
