"""
Gemini Model (:mod:`models.gemini`)
===================================
"""
from __future__ import annotations

from typing_extensions import Optional
import google.generativeai as genai
from google.generativeai.client import _ClientManager
from logging import getLogger

from nbds.models import Model
from nbds.prompt import SYSTEM_PROMPT

__all__ = ["Gemini"]

logger = getLogger(__name__)


class Gemini(Model):
    def __init__(self, api_key: str, model: str = "gemini-1.0-pro"):
        """
        Gemini Model

        Parameters
        ----------
        api_key : str
            API Key.
        model : str, optional
            Model Name. Default is "gemini-pro-1.0"
        """

        # Encapsule client configuration
        cm = _ClientManager()
        cm.configure(api_key=api_key)

        self.m: genai.GenerativeModel = genai.GenerativeModel(model)
        logger.info("Gemini: %s", self.m.model_name)

        self.m._client = cm.get_default_client("generative")
        self.m._async_client = cm.get_default_client("generative_async")

        self.c = self.m.start_chat()

    def __call__(self, prompt: str) -> str:
        """
        Call Gemini Model

        Parameters
        ----------
        prompt : str
            User Request Prompt

        Returns
        -------
        str
            Model Response
        """
        response = self.c.send_message(f"""
==== Start: System Prompt ====
{SYSTEM_PROMPT}
==== Finish: System Prompt ====

==== Start: User Prompt ====
{prompt}
==== Finish: User Prompt ====
""")
        logger.debug("Gemini: %d candidates", len(response.candidates))

        return response.text
