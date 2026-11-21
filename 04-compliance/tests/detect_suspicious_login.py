import csv
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

base = Path(__file__).resolve().parent
source = base / "synthetic-login-events.csv"
output = base / "TEST-002-detection-alerts.csv"

with source.open(newline="") as f:
    events = list(csv.DictReader(f))

for event in events:
    event["dt"] = datetime.fromisoformat(event["timestamp"])

events.sort(key=lambda e: e["dt"])
alerts = []
seen = set()

for event in events:
    if event["status"] != "FAILED":
        continue

    window_start = event["dt"] - timedelta(minutes=5)
    failures = [
        e for e in events
        if e["account_id"] == event["account_id"]
        and e["source_ip"] == event["source_ip"]
        and e["status"] == "FAILED"
        and window_start <= e["dt"] <= event["dt"]
    ]

    key = ("BRUTE_FORCE", event["account_id"], event["source_ip"])
    if len(failures) >= 5 and key not in seen:
        seen.add(key)
        alerts.append({
            "alert_id": f"ALERT-{len(alerts)+1:03d}",
            "rule": "BRUTE_FORCE",
            "account_id": event["account_id"],
            "event_ids": ";".join(e["event_id"] for e in failures),
            "reason": "5 or more failed logins within 5 minutes",
            "severity": "HIGH"
        })

successes = [e for e in events if e["status"] == "SUCCESS"]

for i, current in enumerate(successes):
    for previous in successes[:i]:
        delta = current["dt"] - previous["dt"]

        if (
            current["account_id"] == previous["account_id"]
            and current["country"] != previous["country"]
            and timedelta(0) <= delta <= timedelta(minutes=5)
        ):
            key = (
                "RAPID_COUNTRY_CHANGE",
                previous["event_id"],
                current["event_id"]
            )
            if key not in seen:
                seen.add(key)
                alerts.append({
                    "alert_id": f"ALERT-{len(alerts)+1:03d}",
                    "rule": "RAPID_COUNTRY_CHANGE",
                    "account_id": current["account_id"],
                    "event_ids": previous["event_id"] + ";" + current["event_id"],
                    "reason": "Successful logins from different countries within 5 minutes",
                    "severity": "MEDIUM"
                })

fields = [
    "alert_id", "rule", "account_id",
    "event_ids", "reason", "severity"
]

with output.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(alerts)

print("TRUSTIFY — TEST-002")
print("Events analyzed:", len(events))
print("Alerts generated:", len(alerts))

for alert in alerts:
    print(alert["alert_id"], alert["rule"], alert["account_id"])

print("Evidence saved:", output)
