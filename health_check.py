import psutil
import subprocess
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "health_check.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

def check_cpu():
    usage = psutil.cpu_percent(interval=1)
    status = "WARNING" if usage >= 80 else "OK"
    message = f"CPU usage: {usage}% - {status}"
    print(message)
    logging.info(message)

def check_memory():
    usage = psutil.virtual_memory().percent
    status = "WARNING" if usage >= 80 else "OK"
    message = f"Memory usage: {usage}% - {status}"
    print(message)
    logging.info(message)

def check_disk():
    usage = psutil.disk_usage("/").percent
    status = "WARNING" if usage >= 80 else "OK"
    message = f"Disk usage: {usage}% - {status}"
    print(message)
    logging.info(message)

def check_service(service="nginx"):
    try:
        result = subprocess.run(
            ["systemctl", "is-actice", service],
            capture_output=True,
            text=True,
            timeout=5
        )

        status = result.stdout.strip() or "unknown"
        message = f"Service{service}: {status}"

        print(message)
        logging.info(message)

    except (OSError, subprocess.TimeoutExpired) as error:
        message = f"Service check failed: {error}"
        print(message)
        logging.error(message)

if __name__ == "__main__":
    print("===== SYSTEM HEALTH CHECK =====")

    check_cpu()
    check_memory()
    check_disk()
    check_service("nginx")

    print(f"Log saved to: {LOG_FILE}")
    print("===== CHECK COMPLETED =====")
