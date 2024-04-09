# Notebook Data Scientist (nbds)

> [!CAUTION] 
> This project doesn't work properly, yet.


Notebook Data Scientist (nbds) is a PoC project
to analyze data by Large Language Model (LLM) on Jupyter Notebook.

This project was inspired by [Data Interpreter](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/intro.html).




```python
from nbds.models import Gemini
from nbds import NBDataScientist

api_key = ...
model = Gemini(api_key)

scientist = NBDataScientist(model)
scientist.register_magic()
```


```text
%%nbds
Read "Training Data" and create a model to predict "median_income",
then evaluate the model with "Test Data"

Training Data: ./sample_data/california_housing.csv
Test Data: ./sample_data/california_housing.csv
```

> [!WARNING] 
> We execute LLM-generated code. 
> Every time the code will be displayed and you will be asked before execution. 
> You must check generated code by yourself.
> Additionally, we highly recommend to run separated environment like container,
> and not to analyze any confidential information at all.

