import requests

def query_gemma3(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "gemma3", "prompt": prompt, "stream": False}
    )
    if response.ok:
        data = response.json()
        return data.get("response") or data
    return f"Ollama error: {response.text}"


# print(query_gemma3("Hello, Gemma 3!"))