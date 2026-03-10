from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)

messages = [
    {"role": "system", "content": "You are a helpful AI assistant specialized in AI and programming."}
]

MAX_HISTORY = 10

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    messages.append({"role": "user", "content": user})

    # Limit conversation history
    if len(messages) > MAX_HISTORY:
        messages = [messages[0]] + messages[-MAX_HISTORY:]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=MODEL_NAME
    )

    reply = chat_completion.choices[0].message.content

    print("AI:", reply)

    messages.append({"role": "assistant", "content": reply})