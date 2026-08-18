import subprocess
import sys
import time


# Iniciar FastAPI
api_process = subprocess.Popen(
    [
        sys.executable,
        "-m",
        "uvicorn",
        "api.main:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000"
    ]
)

# Dar tiempo para que FastAPI inicie
time.sleep(3)

# Iniciar Streamlit
streamlit_process = subprocess.Popen(
    [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "app.py",
        "--server.address",
        "0.0.0.0",
        "--server.port",
        "8501"
    ]
)

try:
    api_process.wait()
    streamlit_process.wait()

except KeyboardInterrupt:
    api_process.terminate()
    streamlit_process.terminate()