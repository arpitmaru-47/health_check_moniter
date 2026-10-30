import psutil

cpu_usage = psutil.cpu_percent(interval=1)

print(f"CPU Usage: {cpu_usage}%")

if cpu_usage >= 80:
    print("WARNING: High CPU usage")
else:
    print("OK: CPU usage is normal")
