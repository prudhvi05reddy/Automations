"""
Platform Factory
Detects the host OS and instantiates the matching platform adapter
"""
import sys
from .base import BasePlatform
from .windows import WindowsPlatform
from .macos import MacOSPlatform
from .linux import LinuxPlatform

def get_platform() -> BasePlatform:
    if sys.platform.startswith("win"):
        return WindowsPlatform()
    elif sys.platform.startswith("darwin"):
        return MacOSPlatform()
    else:
        return LinuxPlatform()
