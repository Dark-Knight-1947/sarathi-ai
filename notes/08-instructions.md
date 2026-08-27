# Instructions & Behavior

## 1. What are Instructions?

Instructions tell the AI how it should behave while responding to the user.
In the Responses API, we can provide instructions using the instructions parameter.
These instructions are separate from the user's question

## 2. Flow Diagram

```text
Instructions
     ↓
How should the AI behave?

Input
     ↓
What is the user asking?

     ↓

     AI

     ↓

Response
```


## 3. Instructions Can Change Behavior

The same user input can produce different responses depending on the instructions.


## 4. Why Instructions Matter for Alexa AI

Our goal is not just to make a program that sends questions to an AI model.
We are building a personal voice assistant.

Instructions will allow us to define things such as:

- Personality
- Tone
- Response length
- How information should be explained
- How the assistant should interact with the user

For a voice assistant, concise and conversational responses are especially useful because the responses will eventually be spoken aloud.