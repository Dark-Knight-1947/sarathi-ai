# APIs & API Keys

## 1. What is an API?
API stands for **Application Programming Interface**.
An API is a way for different software programs or systems to communicate with each other and request or exchange information.
A simple way to think about an API is as a **bridge between two software systems**.


## 2. What is an API Key?
An API key is a secret credential used to authenticate API requests and associate those requests with an account or project.
It is similar to a password or access key for an API.

In our project, our Python program needs an OpenAI API key so that OpenAI can identify and authorize our API requests.
An API key should be treated as a secret and should never be publicly exposed.


## 3. How they work together in our project
Our Python program sends a request to the OpenAI API.
The request is authenticated using our API key.

```text
Python Program
      |
      | Request + API Key
      v
  OpenAI API
      |
      v
OpenAI Servers
      |
      v
     GPT
      |
      | Response
      v
  Python Program
