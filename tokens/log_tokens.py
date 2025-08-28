import tiktoken

def log_tokens(prompt, model="gpt-3.5-turbo"):
    enc = tiktoken.encoding_for_model(model)
    tokens = enc.encode(prompt)
    print(f"Token count: {len(tokens)}")
    return tokens

if __name__ == "__main__":
    prompt = "Summarize the following article in three bullet points."
    log_tokens(prompt)
