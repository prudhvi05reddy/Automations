"""
Linux Platform Adapter
Handles browser and application launching on Linux
"""
import shutil
import subprocess
import webbrowser
from pathlib import Path
from .base import BasePlatform

class LinuxPlatform(BasePlatform):
    def is_vscode_installed(self, executable: str = "code") -> bool:
        return shutil.which(executable) is not None

    def open_vscode(self, path: Path, executable: str = "code") -> bool:
        try:
            subprocess.Popen([executable, str(path)])
            return True
        except Exception:
            return False

    def open_url(self, url: str, browser_preference: str = "default") -> bool:
        browser_pref = browser_preference.lower()
        try:
            if browser_pref in ["chrome", "google-chrome"] and shutil.which("google-chrome"):
                subprocess.Popen(["google-chrome", url])
                return True
            elif browser_pref == "firefox" and shutil.which("firefox"):
                subprocess.Popen(["firefox", url])
                return True
            webbrowser.open_new_tab(url)
            return True
        except Exception:
            return False
