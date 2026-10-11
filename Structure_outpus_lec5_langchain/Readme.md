Hey we are in lecture 5 and going to start strucutred output.

Use cases: API Building. Agents. Data Extraction

There are two types of LLMs
1. Those who can generate structure iutput themselves like OpenAI models with the help of 'with_structured_output' function
2. Those who cannot so we have to manually make them generate structured output with the help of output parsing

In lecture 5 we are going to cover 1st type of LLMs based on 3 data formats
1. Typed dictionary: Way to define dictionary in python where you specify what keys and values should exist. It helps ensure that your dictionary follows a specific structure.
2. Pydantic: Pydantic is a data validation and data parsing library for python. It ensures that the data you work with is correct, structured and type-safe.
3. Json_schema: We use json schema, when our project is in more than one language like python in backend and javascript in frontend. Json is a universla schema format.

--Things to remember
with_structured_output have 2 methods -json_mode(returns output in json format) and -function_calling(when we want structured output to call any function from it) (It is default) 