"""
Workspace Profiles Module
Defines target apps, sites, and settings for each workspace mode
"""
from typing import Dict, Any, List
from .config import ConfigManager

class ProfileManager:
    def __init__(self, config: ConfigManager):
        self.config = config

    def get_plan(self, profile_name: str | None = None) -> Dict[str, Any]:
        """Returns the execution plan (URLs, VS Code flag, Notes flag) for the requested profile."""
        if not profile_name or profile_name.lower() in ["default", "startmyday", "full"]:
            # Default full StartMyDay mode
            return {
                "name": "StartMyDay Full Workspace",
                "open_vscode": True,
                "open_notes": self.config.enable_daily_notes,
                "urls": list(self.config.default_urls.values())
            }

        profile_data = self.config.get_profile(profile_name.lower())
        if profile_data:
            return {
                "name": profile_data.get("description", profile_name.title()),
                "open_vscode": profile_data.get("open_vscode", True),
                "open_notes": profile_data.get("open_notes", False) and self.config.enable_daily_notes,
                "urls": profile_data.get("urls", [])
            }

        # Fallback to default if unknown profile is specified
        return {
            "name": f"Custom: {profile_name}",
            "open_vscode": True,
            "open_notes": self.config.enable_daily_notes,
            "urls": list(self.config.default_urls.values())
        }
