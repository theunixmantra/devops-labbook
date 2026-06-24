#!/usr/bin/env python3

import psutil
import socket
import platform
import shutil
from datetime import datetime

def bytes_to_gb(bytes_value):
    return round(bytes_value / (1024 ** 3), 2)

print("=" * 60)
print("        Rocky Linux Server Health Check")
print("=" * 60)

print(f"Hostname        : {socket.gethostname()}")
print(f"OS              : {platform.platform()}")
print(f"Date & Time     : {datetime.now()}")
print("-" * 60)

cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage       : {cpu_usage}%")

memory = psutil.virtual_memory()
print(f"RAM Total       : {bytes_to_gb(memory.total)} GB")
print(f"RAM Used        : {bytes_to_gb(memory.used)} GB")
print(f"RAM Usage       : {memory.percent}%")

swap = psutil.swap_memory()
print(f"Swap Total      : {bytes_to_gb(swap.total)} GB")
print(f"Swap Used       : {bytes_to_gb(swap.used)} GB")
print(f"Swap Usage      : {swap.percent}%")

disk = shutil.disk_usage("/")
disk_percent = round((disk.used / disk.total) * 100, 2)
print(f"Disk Total /    : {bytes_to_gb(disk.total)} GB")
print(f"Disk Used /     : {bytes_to_gb(disk.used)} GB")
print(f"Disk Usage /    : {disk_percent}%")

boot_time = datetime.fromtimestamp(psutil.boot_time())
print(f"Last Boot Time  : {boot_time}")

print("-" * 60)

if cpu_usage > 80:
    print("WARNING: High CPU usage")

if memory.percent > 80:
    print("WARNING: High RAM usage")

if disk_percent > 80:
    print("WARNING: High Disk usage")

if swap.percent > 50:
    print("WARNING: High Swap usage")

print("=" * 60)
print("Health Check Completed")
print("=" * 60)
