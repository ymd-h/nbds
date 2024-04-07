from setuptools import setup, find_packages

setup(name="nbds",
      version="0.0.0",
      description="Notebook Data Scientist",
      packages=find_packages(),
      install_requires=["typing_extensions", "well-behaved-logging"],
      extras_require={
          "gemini": ["google-generativeai"],
      })
