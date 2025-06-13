#!/bin/bash
echo "Disk Usage Report for $(hostname) on $(date)"
df -h | grep -vE '^Filesystem|tmpfs|cdrom' | awk '{print $1, $5, $6}'
