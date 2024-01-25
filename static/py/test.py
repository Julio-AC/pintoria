#use open ai
import streamlit as st
import os
import openai

#openai.api_key = "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"
openai.api_key = os.environ.get("OPENAI_API_KEY")

def chatgpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text
    return message

prompt = input("You: ")
response = chatgpt(prompt)
print("ChatGPT:", response)

