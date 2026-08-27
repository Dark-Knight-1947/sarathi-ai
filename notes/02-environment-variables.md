# Environment Variables

## 1. What is an Environment Variable?

An environment variable is a named value provided by the operating system/environment that programs can read while they are running.
For example, Windows can store a value like:
OPENAI_API_KEY = xxxxxxxxxxxx

Our Python program can then access this value when it runs.


## 2. Why are we using an Environment Variable?

We don't want to write our API key directly inside our Python source code. Instead we store the API key as an environment variable.

Bad:
```python
client = OpenAI(api_key="MY_SECRET_API_KEY")
```

Good:
OPENAI_API_KEY

Our Python program can then use the key without the actual secret appearing in main.py.
This keeps the secret separate from our source code and reduces the chance of accidentally exposing it when sharing the project or pushing it to GitHub.


## 3. How does it work in our project?

```text
Windows
   |
   | OPENAI_API_KEY
   v
Python Program
   |
   | client = OpenAI()
   v
OpenAI Python Library
   |
   | API request + API key
   v
OpenAI API
```

When we create:
```python
client = OpenAI()
``` 
the OpenAI Python library automatically looks for an environment variable named: OPENAI_API_KEY
It retrieves the key from the environment and uses it when making API requests.