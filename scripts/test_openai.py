from app.core.openai_client import client

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "diga apenas: conexão funcionando"}
    ]
)

print(response.choices[0]. message.content)