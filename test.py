from Glogger import Loki
import os
from config import P

creds = P()

logger = Loki(config=creds)
import traceback


try:
    raise KeyError
except Exception as e:
    logger.error("{'asdasd':'asd'}", **{"clientID": "runId1"}, name="test", exception=e)
