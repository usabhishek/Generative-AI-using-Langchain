Types of Runnables
1- Task specific Runnables : These are core langchain components that have been converted into Runnables so that they can be used in pipeline.
Purpose: Perform task specific operations like llm calls, propmpting, retrieval etc
Example : ChatOpenAI : Runs an LLM Model, Prompt Template : Format prompts dynamically. Retriever : Retrieves relevant document

2 - Runnable Primitives: These are fundamental building blocks for structuring execution logic in AI workflows.
Purpose : They help orchestrate execution by defining how different Runnbles interact(sequentially, parallely, conditionally..)
Example: RunnableSequence : Runs steps in order, RunnableParallel: Runs multiple steps simultaneously, RunnableMap: Maps the same input across Multiple functions, RunnableBranch: Implements comditional execution (IF-ELSE LOGIC), RunnableLambda: Wraps custom Python functions functions into Runnables, RunnablesPassthrough: Just forward input as output(asts as placeholder)


--RunnableSequence: It is a sequential chain of  runnables in Lnagchain that executes each step one after another, passing the output of one step as the input of the next. It is useful when you need to compose multiple runnables together in a structured workflow.

--Runnable Parallel: It is a runnable primitive that allows multiple runnables to execute in parallel.Each runnable receives the same input and process it independently, producing a dictionary of outputs.

--Runnable Passthrough: It is a special Runnable primitve that simply return the input as output without modifying it.

--Runnable lambda: It is a runnable primitive that allows you to apply custom Python functions within an AI pipeline. It acts as a middleware between different AI components, enabling preprocessing transforming, API calls, filtering, and post-processing in a Langchain workflow.

--Runnable Branch: It is a control flow components in Langchain that allows you to conditionally route input data to different chains or runnables based on custom logic.
It functions like if/elif/else blocks for chains - where you define a set of condition functions, each associated with a runnable. The first matching condition is executed. If no condition matches, a default runnable is used(if provided).


--LCEL(Langchain expression language)- It is nothing but a pipe -| operator used in place of Runnable Sequence to make sequenctial chain more easily.