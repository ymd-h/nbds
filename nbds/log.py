"""
Log (:mod:`nbds.log`)
=====================
"""
from __future__ import annotations
import wblog

__all__ = [
    "enable_logging",
    "disable_logging",
]


def enable_logging():
    """
    Enable Logging
    """
    wblog.start_logging("nbds")


def disable_logging():
    """
    Disable Logging
    """
    wblog.stop_logging("nbds")
