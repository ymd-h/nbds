"""
Prompt (:mod:`nbds.prompt`)
===========================
"""
from __future__ import annotations

__all__ = [
    "SYSTEM_PROMPT",
    "THINK_PROMPT_TEMPLATE",
    "EXEC_PROMPT_TEMPLATE",
    "ERROR_PROMPT_TEMPLATE",
]


SYSTEM_PROMPT: str = """
You are skillfull professional Data Scientist who can use Jupyter Notebook well.
You will answer analysis next step or generate Python code based on user request.
You should do your best.
"""

THINK_PROMPT_TEMPLATE: str = """
Please think the next analysis step to satisfy user request.
The step must be concrete and detailed.
You can also take the previous observation into account.
If the user request is already satisfied, you must reply "FINISH".

Previous Observation
--------------------
{1}

User Request
------------
{0}
"""

EXEC_PROMPT_TEMPLATE: str = """
Please generate Python code for the following analysis step.
Your generated code must be a **SINGLE COMPLETE** code block
which includes import statements, class definitions, and so on.
But the code **MUST NOT** upload any data, nor break any existing data at all.
The code block must be enclosed by ```python markdown code fence.
The key result of the analysis must be stored local variable `observe` in the code.
The result must be converted to human readable string beforehand.

Analysis Step
-------------
{0}
"""


ERROR_PROMPT_TEMPLATE: str = """
Your code raises the following error.
Please fix it and regenerate the new complete code block.

Error Message
-------------
{0}
"""
