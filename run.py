from app import app
import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", logging.WARNING))

