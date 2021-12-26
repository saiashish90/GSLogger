from Glogger import Loki
from dotenv import load_dotenv
import os

load_dotenv()

logger = Loki(
    url="https://129662:eyJrIjoiMmY1ZjI0MjBkN2FkYjY4MzkwY2M3NTU3M2E3NGVjMTU4ZDc5ZWYzOCIsIm4iOiJweXRob25sb2dnZXIiLCJpZCI6NTY4OTYxfQ==@logs-prod-us-central1.grafana.net/loki/api/v1/push",
)
import traceback

try:
    raise KeyError
except Exception as e:
    logger.error("{'asdasd':'asd'}", **{"clientID": "runId1"}, name="test")
