from lib import Loki
from dotenv import load_dotenv
import os

load_dotenv()

logger = Loki()
import traceback

try:
    raise KeyError
except Exception as e:
    logger.error("{'asdasd':'asd'}", **{"clientID": "runId1"}, name="test")
