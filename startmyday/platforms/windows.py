"""
Windows Platform Adapter
Handles browser and application launching on Windows OS
"""
import os
import shutil
import subprocess
import webbrowser
from pathlib import Path
from .base import BasePlatform

class WindowsPlatform(BasePlatform):
    def is_vscode_installed(self, executable: str = "code") -> bool:
        if shutil.which(executable):
            return True
        # Check standard default installation paths on Windows
        local_app_data = os.environ.get("LOCALAPPDATA", "")
        if local_app_data:
            common_path = Path(local_app_data) / "Programs" / "Microsoft VS Code" / "Code.exe"
            if common_path.exists():
                return True
        return False

    def open_vscode(self, path: Path, executable: str = "code") -> bool:
        try:
            # Check executable or use detected path
            cmd = executable
            if not shutil.which(cmd):
                local_app_data = os.environ.get("LOCALAPPDATA", "")
                if local_app_data:
                    candidate = Path(local_app_data) / "Programs" / "Microsoft VS Code" / "Code.exe"
                    if candidate.exists():
                        cmd = str(candidate)

            subprocess.Popen([cmd, str(path)], shell=True)
            return True
        except Exception:
            return False

    def open_url(self, url: str, browser_preference: str = "default") -> bool:
        browser_pref = browser_preference.lower()
        try:
            if browser_pref in ["edge", "msedge"]:
                # Use msedge launcher on Windows if available
                subprocess.Popen(f'start msedge "{url}"', shell=True)
                return True
            elif browser_pref in ["chrome", "google-chrome"]:
                if shutil.which("chrome"):
                    subprocess.Popen(f'start chrome "{url}"', shell=True)
                    return True
            elif browser_pref == "firefox":
                if shutil.which("firefox"):
                    subprocess.Popen(f'start firefox "{url}"', shell=True)
                    return True

            # Universal standard fallback
            webbrowser.open_new_tab(url)
            return True
        except Exception:
            try:
                webbrowser.open_new_tab(url)
                return True
            except Exception:
                return False
