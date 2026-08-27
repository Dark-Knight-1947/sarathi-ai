# OpenAI Python SDK

## 1. What is a Library?

A library is a collection of pre-written code that other programmers can use in their own programs.
Instead of writing everything from scratch, we can use functions, classes, and other code provided by a library.
For example, instead of manually building all the code required to communicate with OpenAI's servers, we can use the OpenAI Python library.


## 2. What is an SDK?

SDK stands for **Software Development Kit**.
An SDK is a collection of tools, libraries, and code that makes it easier to build applications for a particular platform or service.
The OpenAI Python SDK provides Python code that makes it easier for our Python program to communicate with the OpenAI API.


## 3. Installing & Importing the OpenAI Python Library

We installed the OpenAI Python package using:

```powershell
pip install openai
```

and imported the OpenAI class from openai library 


## 4. Creating the Client

We create an object from the OpenAI class:
```python
client = OpenAI()
```

Here:
* OpenAI is a class provided by the OpenAI Python SDK.
* OpenAI() creates an object (instance) of that class.
* client is the variable that stores that object.


## 5. How everything works:
```text 
Our Python Program
       |
       | uses
       v
OpenAI Python SDK
       |
       | sends API request
       v
OpenAI API
       |
       v
OpenAI Servers
       |
       v
     GPT