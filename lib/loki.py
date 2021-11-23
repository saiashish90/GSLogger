import requests
import json
import time
import os

curr_datetime = time.time_ns()

# initialize the loki client class
class Loki:
    def __init__(self):
        try:
            url = os.environ["LOKI_URL"]
        except KeyError:
            print("Please set the LOKI_URL environment variable")
            exit(1)
        self.url = url

    # function to post logs to loki
    def info(self, msg, **tags):
        # Constructing the payload
        curr_datetime = time.time_ns()
        payload = json.dumps(
            {"streams": [{"stream": tags, "values": [[curr_datetime, f"[INFO] {msg}"]]}]}
        )
        # Posting the payload
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.url, data=payload, headers=headers)
        if r.status_code != 204:
            print("Error posting to Loki")
        else:
            print(f"[INFO] {msg}")

    def warning(self, msg, **tags):
        # Constructing the payload
        curr_datetime = time.time_ns()
        payload = json.dumps(
            {"streams": [{"stream": tags, "values": [[curr_datetime, f"[WARNING] {msg}"]]}]}
        )
        # Posting the payload
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.url, data=payload, headers=headers)
        if r.status_code != 204:
            print("Error posting to Loki")
        else:
            print(f"[WARNING] {msg}")

    def error(self, msg, **tags):
        # Constructing the payload
        curr_datetime = time.time_ns()
        payload = json.dumps(
            {"streams": [{"stream": tags, "values": [[curr_datetime, f"[ERROR] {msg}"]]}]}
        )
        # Posting the payload
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.url, data=payload, headers=headers)
        if r.status_code != 204:
            print("Error posting to Loki")
        else:
            print(f"[ERROR] {msg}")
