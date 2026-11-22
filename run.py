import subprocess
import time

# Start FastAPI Backend
backend = subprocess.Popen(
    ["uvicorn", "main:app", "--reload"],
    cwd="backend",
    shell=True
)

time.sleep(3)

# Start React Frontend
frontend = subprocess.Popen(
    ["npm", "start"],
    cwd="frontend",
    shell=True
)

print("===================================")
print("BOIA Student System Started")
print("Backend : http://localhost:8000")
print("Frontend: http://localhost:3000")
print("===================================")

backend.wait()
frontend.wait()