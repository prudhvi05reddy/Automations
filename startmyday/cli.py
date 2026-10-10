"""
CLI Entry Point for StartMyDay
Provides command-line arguments, profiles, help, and version flags
"""
import argparse
import sys
from pathlib import Path

from . import __version__
from .launcher import WorkspaceLauncher

def main():
    parser = argparse.ArgumentParser(
        prog="startmyday",
        description="StartMyDay - Personal Command-Driven Workspace Automation Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Available profiles:
  startmyday              Start default daily workspace
  startmyday coding       Open coding workspace (VS Code, GitHub, LeetCode, ChatGPT)
  startmyday study        Open study workspace (VS Code, study notes, ChatGPT)
  startmyday placement    Open placement workspace (VS Code, LeetCode, GitHub, LinkedIn, Gmail, Outlook)

Flags:
  --version               Show application version
  --help                  Show this help menu
        """
    )

    parser.add_argument(
        "profile",
        nargs="?",
        default="startmyday",
        help="Optional workspace profile name (e.g., coding, study, placement)"
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"StartMyDay v{__version__}"
    )

    args = parser.parse_args()

    # Determine project root path
    project_root = Path(__file__).resolve().parent.parent
    launcher = WorkspaceLauncher(project_root)
    launcher.launch(args.profile)

if __name__ == "__main__":
    main()
