"""Verify a fictional invoice total from this directory's expenses.json."""
import json
from pathlib import Path


def main():
    data = json.loads(Path(__file__).with_name("expenses.json").read_text())
    expenses = data["expenses"]
    ids = [item["id"] for item in expenses]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate expense ID")
    total = sum(item["amount"] for item in expenses)
    if total != data["claimed_total"]:
        raise SystemExit(f"total mismatch: computed {total}, claimed {data['claimed_total']}")
    print(f"OK total={total}; entries={len(expenses)}")


if __name__ == "__main__":
    main()
