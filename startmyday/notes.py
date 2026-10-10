"""
Daily Notes Generator Module
Creates and manages daily markdown planning notes
"""
from datetime import datetime
from pathlib import Path

NOTE_TEMPLATE = """# {formatted_date}

## 🎯 Today's Goals

- [ ] LeetCode problem
- [ ] Project work
- [ ] Study
- [ ] Job/internship applications

## 🧠 LeetCode

Problem:
Difficulty:
Status:

## 💻 Project Work

Project:
Tasks:

## 📚 Study

Topic:
What I learned:

## 📝 Notes

-

## 🌙 End of Day

Completed:
-

Problems:
-

Tomorrow:
-
"""

class NotesManager:
    def __init__(self, notes_dir: Path):
        self.notes_dir = notes_dir
        self.notes_dir.mkdir(parents=True, exist_ok=True)

    def get_or_create_today_note(self) -> Path:
        today = datetime.now()
        date_str = today.strftime("%Y-%m-%d")
        note_file = self.notes_dir / f"{date_str}.md"

        if not note_file.exists():
            formatted_date = today.strftime("%B %d, %Y")
            content = NOTE_TEMPLATE.format(formatted_date=formatted_date)
            note_file.write_text(content, encoding="utf-8")

        return note_file
