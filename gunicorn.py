import os

from dotenv import load_dotenv

load_dotenv()

bind = "127.0.0.1:8000"
reload = bool(int(os.environ["DEBUG"]))
loglevel = os.environ["LOG_LEVEL"]
workers = os.environ["WORKERS"]
accesslog = "-"
