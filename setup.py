from setuptools import setup, find_packages

setup(name="nbds",
      version="0.0.0",
      description="Notebook Data Scientist",
      packages=find_packages(),
      install_requires=["typing_extensions", "well-behaved-logging", "ipython"],
      extras_require={
          "jupyter": ["jupyter"],
          "gemini": ["google-generativeai"],
      })
