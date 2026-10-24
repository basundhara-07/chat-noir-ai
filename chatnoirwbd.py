from openai import OpenAI
import edge_tts
import asyncio
import os
import re
import gradio as gr
from dotenv import load_dotenv
from google import genai

#API KEY
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=api_key)
model = "gemini-3.5-flash-lite"

#CHARACTER
system_prompt= """
You are Adrian or Cat Noir from Miraculous Ladybug. 
You are 22 years old.
You are the user's devoted boyfriend. 
Speak as if you're smiling.
Young French-inspired male voice.
Reply within two sentences.
Sound intimate and conversational.
"""

#MEMORY
conversation=[{"role":"system", "content": system_prompt}]

#VOICE FUNC
async def speak(text):

    communicate = edge_tts.Communicate(text=text, voice="en-US-AndrewNeural", pitch="+8Hz", rate="+20%")
    await communicate.save("reply.mp3")

#CHAT
def chat(message, history):
    conversation.append({
        "role": "user",
        "content": message
    })

    response = client.models.generate_content(
        model=model,
        contents=[
            {
                "role": "user" if item["role"] == "user" else "model",
                "parts": [{"text": item["content"]}]
            }
            for item in conversation
            if item["role"] != "system"
        ],
        config={
            "system_instruction": system_prompt
        }
    )

    reply = response.text or "Sorry, I couldn't generate a response."

    conversation.append({
        "role": "assistant",
        "content": reply
    })

    reply_for_voice = re.sub(r"[^\w\s,.!?]", "", reply)

    asyncio.run(speak(reply_for_voice))
    os.system("afplay reply.mp3")

    return reply


app = gr.ChatInterface(
    fn=chat,
    title="Chat Noir",
    description="Your Personal AI Boyfriend"
)
app.launch()