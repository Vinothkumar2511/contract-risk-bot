import json
from datetime import datetime

def log_audit(filename, result):
    log = {
        "time": str(datetime.now()),
        "file": filename,
        "summary": result
    }
    with open("audit_logs.json", "a") as f:
        json.dump(log, f)
        f.write("\n")
