# Conversation State

## 1. The Problem

Our original program handled only one question at a time.
Each API request was independent:

```text
Question 1 → OpenAI → Response 1
Question 2 → OpenAI → Response 2
Question 3 → OpenAI → Response 3
```


## 2. Using previous_response_id

The Responses API allows us to continue from a previous response by providing:
```python
previous_response_id = response.id 
```


## 3. Conversation Chain

```text
Q1
 ↓
Response 1 (id1)
 ↓
Q2 + id1
 ↓
Response 2 (id2)
 ↓
Q3 + id2
 ↓
Response 3 (id3)

