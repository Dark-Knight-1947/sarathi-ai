# Context & Memory 

## 1. What is context?

Context is the information available to the AI when generating a response. 
In our project, previous conversation turns can be continued using:
```python
previous_response_id = response.id
```


## 2. What is a Context Window?

A context window is the maximum amount of information, measured in tokens, that a model can handle as context for a request.
A model does not have unlimited context.
As a conversation becomes longer, more tokens may be involved in processing later requests.


## 3. Context vs Memory

Context and memory are related but are not the same thing.
Context --> information available to the model for a current response.
Memory --> information that we deliberately preserve so it can be used later.

A conversation can provide context without being a permanent memory system.


## 4. What is Context Management?
Context management means controlling what information is provided to the model as a conversation grows.

A long-running AI assistant may need to:

- Keep recent messages
- Remove irrelevant old information
- Summarize older conversations
- Store important information separately
- Retrieve relevant information when needed
