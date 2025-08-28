# Token Logging Example

## What are Tokens?
Tokens are the basic units of text that language models process. A token can be as short as one character or as long as one word (e.g., "a", "cat"). Tokenization is the process of splitting text into these units.

## Example: Logging Token Usage
Below is a Python example using the `tiktoken` library (for OpenAI models) to log the number of tokens used in each AI call.

```python
import tiktoken

def log_tokens(prompt, model="gpt-3.5-turbo"):
    enc = tiktoken.encoding_for_model(model)
    tokens = enc.encode(prompt)
    print(f"Token count: {len(tokens)}")
    return tokens

# Example usage:
prompt = "Summarize the following article in three bullet points."
log_tokens(prompt)
```

---
This file explains tokens, tokenization, and demonstrates how to log token usage after every AI call in the KnowledgeDiscoveryAI project.
