import csv
import os

FEEDBACK_FILE = os.path.join(os.path.dirname(__file__), "feedback_log.csv")

def save_feedback(query, response, feedback, comments):
    file_exists = os.path.isfile(FEEDBACK_FILE)
    with open(FEEDBACK_FILE, mode="a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["query", "response", "feedback", "comments"])
        writer.writerow([query, response, feedback, comments])