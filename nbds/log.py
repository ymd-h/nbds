"""
Log (:mod:`nbds.log`)
=====================
"""
from __future__ import annotations
from logging import Handler

from typing_extensions import List, Optional, Union
import wblog

__all__ = [
    "enable_logging",
    "disable_logging",
]

logger = wblog.getLogger()


def enable_logging(level: Optional[int] = None, *,
                   handlers: Optional[Union[Handler, List[Handler]]] = None,
                   propagate: bool = False):
    """
    Enable Logging
    """
    wblog.start_logging("nbds", level, handlers = handlers, propagate = propagate)
    logger.info("Enable Logging")


def disable_logging():
    """
    Disable Logging
    """
    logger.info("Disable Logging")
    wblog.stop_logging("nbds")
