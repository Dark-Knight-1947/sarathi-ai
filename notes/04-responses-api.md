# OpenAI Responses API

## 1. What is the Responses API?

The Responses API is an OpenAI API that allows our application to send input to an OpenAI model and receive a response.
In our project, we use it to send the user's question to the AI and get an answer back.


## 2. How do we use it?

Our code is:

```python
response = client.responses.create(
    model="gpt-5.6-luna",
    input=question,
    max_output_tokens=30
)
```

The responses.create() method creates an API request. Further, we provide them which model do we want to use & what's the input.
max_output_tokens set a maximum number of tokens that a model can generate in its output.


## 3. Getting the AI's answer

The response object contains information about the API response. 
To get the generated text, we use:
```python
response.output_text
```

## 4. The Complete Flow

```text
question = input("You: ")
        |
        v
client.responses.create()
        |
        | model
        | input
        | max_output_tokens
        v
   OpenAI API
        |
        v
   AI Model
        |
        v
 Response object
        |
        v
response.output_text
        |
        v
    print()
        |
        v
   User sees answer