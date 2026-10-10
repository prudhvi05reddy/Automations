"""
StartMyDay Configuration Module
Loads, validates, and manages config.json
"""
import json
import os
from pathlib import Path
from typing import Dict, Any

DEFAULT_CONFIG: Dict[str, Any] = {
    "browser": "edge",
    "vscode_command": "code",
    "project_folder": str(Path(__file__).resolve().parent.parent),
    "enable_daily_notes": True,
    "urls": {
        "leetcode": "https://leetcode.com",
        "github": "https://github.com",
        "chatgpt": "https://chatgpt.com",
        "gmail": "https://mail.google.com",
        "outlook": "https://outlook.live.com",
        "whatsapp": "https://web.whatsapp.com"
    },
    "profiles": {
        "coding": {
            "description": "Coding Workspace",
            "open_vscode": true if hasattr(__builtins__, 'true') else True,
            "open_notes": False,
            "urls": [
                "https://leetcode.com",
                "https://github.com",
                "https://chatgpt.com"
            ]
        },
        "study": {
            "description": "Study Workspace",
            "open_vscode": True,
            "open_notes": True,
            "urls": [
                "https://chatgpt.com"
            ]
        },
        "placement": {
            "description": "Placement & Career Workspace",
            "open_vscode": True,
            "open_notes": True,
            "urls": [
                "https://leetcode.com",
                "https://github.com",
                "https://mail.google.com",
                "https://outlook.live.com",
                "https://www.linkedin.com"
            ]
        }
    }
}

class ConfigManager:
    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not self.config_path.exists():
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                config = DEFAULT_CONFIG.copy()
                config.update(loaded)
                return config
        except Exception:
            return DEFAULT_CONFIG.copy()

    @property
    def browser(self) -> str:
        return self.data.get("browser", "edge")

    @property
    def vscode_command(self) -> str:
        return self.data.get("vscode_command", "code")

    @property
    def project_folder(self) -> Path:
        raw_path = self.data.get("project_folder")
        if raw_path:
            return Path(raw_path)
        return self.config_path.parent

    @property
    def enable_daily_notes(self) -> bool:
        return bool(self.data.get("enable_daily_notes", True))

    @property
    def default_urls(self) -> Dict[str, str]:
        return self.data.get("urls", DEFAULT_CONFIG["urls"])

    def get_profile(self, profile_name: str) -> Dict[str, Any] | None:
        profiles = self.data.get("profiles", {})
        return profiles.get(profile_name)
