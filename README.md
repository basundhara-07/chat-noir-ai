# Chat Noir: Your Personal AI Boyfriend

Chat Noir is a conversational AI chatbot, inspired by the charm and playful personality of Cat Noir from *Miraculous Ladybug*. Built with Python, Google Gemini, and Gradio, it offers an interactive chat experience with optional text-to-speech responses. This project is just for fun.

## ⭐️Features

- **AI-powered conversations** using the Google Gemini API
- **Character-based personality** with a playful, affectionate conversational style
- **Interactive web interface** powered by Gradio
- **Text-to-speech** using Edge TTS
- **Environment-based API key management** to keep credentials out of source code

## ⭐️Tech Stack

- Python
- Google Gemini API (`google-genai`)
- Gradio
- Edge TTS
- python-dotenv

## ⭐️Run Locally

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_REPOSITORY_NAME
```

### 2. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 3. Configure your API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace the placeholder with your own Gemini API key.

### 4. Launch the application

```bash
python3 chatnoirwbd.py
```

Open the local Gradio URL printed in your terminal.

