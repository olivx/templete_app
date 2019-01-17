import os

from dotenv import load_dotenv

load_dotenv()

bind = "0.0.0.0:8000"
reload = bool(int(os.environ["DEBUG"]))
loglevel = os.environ["LOG_LEVEL"]
workers = os.environ["WORKERS"]
accesslog = "-"
