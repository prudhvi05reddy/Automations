"""
Base Platform Adapter Interface
Defines common contract for OS-specific desktop & browser interactions
"""
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

class BasePlatform(ABC):
    @abstractmethod
    def open_url(self, url: str, browser_preference: str = "default") -> bool:
        """Opens a single URL in the requested or default browser."""
        pass

    @abstractmethod
    def open_vscode(self, path: Path, executable: str = "code") -> bool:
        """Opens VS Code pointing to the given file or directory."""
        pass

    @abstractmethod
    def is_vscode_installed(self, executable: str = "code") -> bool:
        """Checks if VS Code executable is accessible."""
        pass
