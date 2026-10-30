import psutil

memory = psutil.virtual_memory()

print(f"Total Memory:{memory.total / (1024**3):.2f}GB")
print(f"Used Memory: {memory.percent}%")

if memory.percent >= 80:
    print("WARNING: High memory usage")
else:
    print("OK: Memory usage is normal")
