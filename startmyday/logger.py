"""
StartMyDay Logging Module
Records actions, commands, and errors to logs/startmyday.log
"""
import logging
import os
from pathlib import Path

def setup_logger(log_dir: Path) -> logging.Logger:
    """Configures file and stream logging for StartMyDay."""
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "startmyday.log"

    logger = logging.getLogger("StartMyDay")
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if setup is called multiple times
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
