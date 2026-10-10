"""
Workspace Launcher Module
Coordinates execution, browser tabs, VS Code, notes, and UI display
"""
import time
from pathlib import Path
from typing import Dict, Any, List

from .config import ConfigManager
from .logger import setup_logger
from .notes import NotesManager
from .profiles import ProfileManager
from .platforms import get_platform

def format_site_label(url: str) -> str:
    """Provides a friendly label for common workspace URLs."""
    url_lower = url.lower()
    if "leetcode" in url_lower:
        return "LeetCode"
    if "github" in url_lower:
        return "GitHub"
    if "chatgpt" in url_lower:
        return "ChatGPT"
    if "mail.google" in url_lower or "gmail" in url_lower:
        return "Gmail"
    if "outlook" in url_lower:
        return "Outlook"
    if "whatsapp" in url_lower:
        return "WhatsApp Web"
    if "linkedin" in url_lower:
        return "LinkedIn"
    
    # Strip protocol and domain for generic names
    cleaned = url.split("//")[-1].split("/")[0].replace("www.", "")
    return cleaned.capitalize()

class WorkspaceLauncher:
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.config_manager = ConfigManager(root_dir / "config.json")
        self.logger = setup_logger(root_dir / "logs")
        self.platform = get_platform()
        self.notes_manager = NotesManager(root_dir / "daily_notes")
        self.profile_manager = ProfileManager(self.config_manager)

    def launch(self, profile_name: str | None = None):
        plan = self.profile_manager.get_plan(profile_name)
        mode_title = plan["name"]
        
        self.logger.info(f"StartMyDay launched with mode: {mode_title}")
        print("\n🚀 Starting StartMyDay...")
        print(f"📌 Profile: {mode_title}\n")

        results: List[tuple[bool, str]] = []

        # 1. Open VS Code Project
        if plan["open_vscode"]:
            project_path = self.config_manager.project_folder
            if self.platform.is_vscode_installed(self.config_manager.vscode_command):
                if self.platform.open_vscode(project_path, self.config_manager.vscode_command):
                    results.append((True, "VS Code Workspace"))
                    self.logger.info(f"VS Code launched at {project_path}")
                else:
                    results.append((False, "VS Code Workspace"))
                    self.logger.error("Failed to launch VS Code")
            else:
                results.append((False, "VS Code (Not found in PATH or standard directory)"))
                print("⚠️  Notice: VS Code executable was not found. Install it or update config.json.")
                self.logger.warning("VS Code executable not found.")

        # 2. Open Websites in Browser Tabs
        browser_pref = self.config_manager.browser
        for url in plan["urls"]:
            label = format_site_label(url)
            success = self.platform.open_url(url, browser_preference=browser_pref)
            results.append((success, label))
            if success:
                self.logger.info(f"{label} opened ({url})")
            else:
                self.logger.error(f"Failed to open {label} ({url})")
            time.sleep(0.2)  # Smooth tab opening

        # 3. Open Today's Notes
        if plan["open_notes"]:
            try:
                today_note = self.notes_manager.get_or_create_today_note()
                # Open today's note file in VS Code
                self.platform.open_vscode(today_note, self.config_manager.vscode_command)
                results.append((True, "Today's Notes"))
                self.logger.info(f"Daily note opened: {today_note.name}")
            except Exception as e:
                results.append((False, "Today's Notes"))
                self.logger.error(f"Failed to open today's notes: {e}")

        # Display Summary Box
        self._print_summary_card(results)
        self.logger.info("StartMyDay workspace launch completed")

    def _print_summary_card(self, results: List[tuple[bool, str]]):
        box_width = 46
        inner_width = box_width - 2

        print("\n" + "╔" + "═" * inner_width + "╗")
        title = "🚀 START MY DAY"
        print(f"║{title.center(inner_width)}║")
        print("╠" + "═" * inner_width + "╣")
        print("║" + " " * inner_width + "║")

        for success, label in results:
            icon = "✓" if success else "✗"
            line_text = f" {icon} {label}"
            padding = inner_width - len(line_text)
            print(f"║{line_text}{' ' * max(0, padding)}║")

        print("║" + " " * inner_width + "║")
        footer = "Workspace Ready!"
        print(f"║{footer.center(inner_width)}║")
        print("║" + " " * inner_width + "║")
        print("╚" + "═" * inner_width + "╝\n")
