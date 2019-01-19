import os

from dotenv import load_dotenv

load_dotenv()

bind = "0.0.0.0:8000"
reload = bool(int(os.environ.get("DEBUG", 0)))
loglevel = os.environ.get("LOG_LEVEL", "INFO")
workers = os.environ["WORKERS"]
accesslog = "-"
