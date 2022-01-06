from Glogger import Loki
import os


logger = Loki(
)
import traceback

try:
    raise KeyError
except Exception as e:
    logger.error("{'asdasd':'asd'}", **{"clientID": "runId1"}, name="test", exception=e)
