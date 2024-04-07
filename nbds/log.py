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


def enable_logging(level: Optional[int] = None, *,
                   handlers: Optional[Union[Handler, List[Handler]]] = None,
                   propagate: bool = False):
    """
    Enable Logging
    """
    wblog.start_logging("nbds", lebel, handlers = handlers, propagate = propagate)


def disable_logging():
    """
    Disable Logging
    """
    wblog.stop_logging("nbds")
