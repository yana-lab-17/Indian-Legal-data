import google.generativeai as genai

genai.configure(api_key="")

model = genai.GenerativeModel("models/gemini-2.5-flash")

with open("legal_text.txt", "r", encoding="utf-8") as file:
    legal_text = file.read()

question = input("Ask a legal question: ")

prompt = f"""
You are a legal assistant.

Legal Section:
{legal_text}

Question:
{question}

Answer only using the provided legal section.
"""

try:
    response = model.generate_content(prompt)

    print("\nAnswer:")
    print(response.text)

except Exception as e:
    print("Error:", e)