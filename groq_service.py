from config import API_key,API_URL
import requests
def ask_groq(prompt):
    headers = {
        "Authorization": f"Bearer {API_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload
    )

    data= response.json()

    return data["choices"][0]["message"]["content"]