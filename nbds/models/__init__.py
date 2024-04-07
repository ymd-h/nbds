"""
Models (:mod:`nbds.models`)
===========================
"""
from __future__ import annotations


__all__ = ["Model"]


class Model:
    def __call__(self, prompt: str) -> str:
        """
        Call Model

        Parameters
        ----------
        prompt : str
            User Request Prompt

        Returns
        -------
        str
            Model Response
        """
        raise NotImplementedError
