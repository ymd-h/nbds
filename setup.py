import os
from setuptools import setup, find_packages

with open("./README.md") as f:
    long_description = f.read()

setup(name="nbds",
      version="0.0.0",
      description="Notebook Data Scientist",
      long_description = long_description,
      long_description_content_type = "text/markdown",
      packages=find_packages(),
      install_requires=["typing_extensions", "well-behaved-logging", "ipython"],
      extras_require={
          "jupyter": ["jupyter"],
          "gemini": ["google-generativeai"],
      })
