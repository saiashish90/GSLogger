from lib import Loki
from dotenv import load_dotenv
import os

load_dotenv()

logger = Loki()
logger.info("This is a test message", **{"clientID": "runId"}, name="test")
