# human_loop/feedback_manager.py

import os
from datetime import datetime

HITL_LOG_PATH = os.path.join("data", "hitl_logs")

def log_human_feedback(version_id, feedback):
    os.makedirs(HITL_LOG_PATH, exist_ok=True)
    log_file = os.path.join(HITL_LOG_PATH, f"feedback_{version_id}.txt")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.now()}] {feedback}\n")

def collect_feedback(text, version_id=None):
    print("\n🧠 AI-generated content:")
    print("="*40)
    print(text)
    print("="*40)

    while True:
        choice = input("Would you like to edit this text? (y/n): ").strip().lower()
        if choice == 'y':
            print("Enter your updated version (end input with a blank line):")
            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)
            edited_text = "\n".join(lines)
            if version_id:
                log_human_feedback(version_id, edited_text)
            return edited_text
        elif choice == 'n':
            if version_id:
                log_human_feedback(version_id, text)
            return text
        else:
            print("Please enter 'y' or 'n'.")
