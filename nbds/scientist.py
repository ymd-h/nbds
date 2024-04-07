"""
Data Scientist (:mod:`nbds.scientist`)
======================================
"""
from __future__ import annotations
import re

from typing_extensions import Any, Dict, Optional
from IPython.core.magic import register_cell_magic
import wblog

from nbds.prompt import THINK_PROMPT_TEMPLATE, ERROR_PROMPT_TEMPLATE
from nbds.models import Model

__all__ = ["NBDataScientist"]


CODE: re.Pattern = re.compile(r"""```python
(.*)
```""", re.DOTALL)

logger = wblog.getLogger()


class NBDataScientist:
    def __init__(self, model: Model, *, max_retry: int = 3):
        """
        Notebook Data Scientist

        Parameters
        ----------
        model : nbds.models.Model
            LLM Model
        max_retry : int, optional
            Max Retry when error happens
        """
        self.model: Model = model
        self.max_retry: int = max_retry
        self.variables: Dict[str, Any] = {}

    def analyze(self, prompt: str) -> None:
        """
        Analyze

        Parameters
        ----------
        prompt : str
            User Request Prompt
        """
        observe: Optional[str] = None
        while True:
            action: Optional[str] = self.think(prompt, observe)
            if action is None:
                return

            observe = self.exec(action)

    def think(self, prompt: str, observe: Optional[str] = None) -> Optional[str]:
        """
        Think Next Step

        Parameters
        ----------
        prompt : str
            User Request Prompt
        observe : str, optional
            Observation of previous step, if exists.

        Returns
        -------
        str, optional
            Next action prompt
        """
        response: str = self.model(THINK_PROMPT_TEMPLATE.format(prompt, observe))
        logger.debug("Model Response\n%s", response)

        if "FINISH" in response:
            return None

        return response


    def exec(self, action: str) -> str:
        """
        Execute Code

        Parameters
        ----------
        action : str
            User Request Prompt

        Returns
        -------
        str
            Result
        """
        for i in range(self.max_retry):
            response: str = self.model(action)
            logger.debug("Model Response\n%s", response)

            code: Optional[re.Match] = CODE.search(response)
            if code is None:
                raise ValueError("Model Response doesn't contain Python Code")

            try:
                exec(code[0], globals = self.variables)
                logger.debug("Global Variables: %s", list(self.variables))

                observe: str = self.variables.get("observe", None)
                logger.debug("Observe: %s", observe)

                return observe
            except e:
                logger.error("Code Exec Error\n%s", e)
                action = ERROR_PROMPT_TEMPLATE.format(e)
        else:
            raise ValueError(f"Maximum Retry Error: {self.max_retry}")


    def register_magic(self) -> None:
        """
        Register Jupyter Cell Magic `%%nbds`
        """
        @register_cell_magic
        def nbds(line: str, cell: str):
            return self.analyze(cell)
