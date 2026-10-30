import subprocess

service = "nginx"

result = subprocess.run(
    ["systemctl", "is-active", service],
    capture_output=True,
    text=True
)

status = result.stdout.strip()

print(f"Service: {service}")
print(f"Status: {status}")

if result.returncode == 0:
    print("OK: Service is active")
else:
    print("WARNING: Service is not active")
    print(result.stderr.strip())
