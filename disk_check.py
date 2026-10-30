import psutil

disk = psutil.disk_usage("/")

print(f"Total Disk: {disk.total /(1024**3):.2f} GB")
print(f"Used Disk: {disk.percent}%")

if disk.percent >= 80:
    print("WARNING: Disk usage is high")
else:
    print("OK: Disk usage is normal")
