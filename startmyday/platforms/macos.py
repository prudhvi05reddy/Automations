"""
macOS Platform Adapter
Handles browser and application launching on macOS
"""
import shutil
import subprocess
import webbrowser
from pathlib import Path
from .base import BasePlatform

class MacOSPlatform(BasePlatform):
    def is_vscode_installed(self, executable: str = "code") -> bool:
        if shutil.which(executable):
            return True
        return Path("/Applications/Visual Studio Code.app").exists()

    def open_vscode(self, path: Path, executable: str = "code") -> bool:
        try:
            if shutil.which(executable):
                subprocess.Popen([executable, str(path)])
                return True
            subprocess.Popen(["open", "-a", "Visual Studio Code", str(path)])
            return True
        except Exception:
            return False

    def open_url(self, url: str, browser_preference: str = "default") -> bool:
        browser_pref = browser_preference.lower()
        try:
            if browser_pref in ["chrome", "google-chrome"]:
                subprocess.Popen(["open", "-a", "Google Chrome", url])
                return True
            elif browser_pref == "edge":
                subprocess.Popen(["open", "-a", "Microsoft Edge", url])
                return True
            elif browser_pref == "firefox":
                subprocess.Popen(["open", "-a", "Firefox", url])
                return True
            elif browser_pref == "safari":
                subprocess.Popen(["open", "-a", "Safari", url])
                return True
            webbrowser.open_new_tab(url)
            return True
        except Exception:
            return False
