 Output Parsers in Langchain help convert raw LLM responses into structures formats like JSON, CSV, Pydantic models and more. They ensure consistency, validation and ease of use in application.

 They can work with both can model(with_structured_output models) and can't model.

 Major output Parsers we will cover -
 string output Parser: Simplest output parser in Langchain. It is used to parse the output of a llm and return it as a plane string.

 json output Parser: We can't able to enforce schema in json output parser. Model will decide to choose the schema according to prompt.

 structured output parser:Is is a output parser in langchain that helps extract structures JSON data from LLM responses based on field schemas.It works by defining a list of fields (Response Schema) that the model should return, ensuring the output follows astructured output.
 
 pydantic output parser: It is a structured output parser in langchain that uses pydantic models to enforce schema validation when processing LLM responses. It ensures strict schema enforcement, type safety, easy validation, seamless integration.