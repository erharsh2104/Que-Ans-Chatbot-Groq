<div align="center">

# Q&A Chatbot with Groq

*Ask a question, get an answer, fast.*

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-green)
![Groq](https://img.shields.io/badge/Powered%20by-Groq-orange)

</div>

---

## What is this?

A small chatbot built with **Streamlit** and **LangChain**. You type a question, pick a model, and **Groq** answers it quickly.

## Features

- Simple question-and-answer interface
- Paste your own Groq API key in the sidebar (it's hidden as you type)
- Choose between different Groq models
- Adjust the **temperature** (how creative the answers are)
- Adjust **max tokens** (how long the answers can be)

## Tech Stack

| Tool | What it does |
|------|--------------|
| Python 3.10 | The language |
| Streamlit | The web interface |
| LangChain | Connects the prompt, model and output |
| Groq | Runs the language model |

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/erharsh2104/Que-Ans-Chatbot-Groq.git
cd Que-Ans-Chatbot-Groq
```

### 2. Create an environment

```bash
conda create -p venv python=3.10 -y
conda activate ./venv
```

### 3. Install the requirements

```bash
pip install -r requirements.txt
```

### 4. Get a free Groq API key

Create one at [console.groq.com/keys](https://console.groq.com/keys).

### 5. Run the app

```bash
streamlit run app.py
```

Then paste your API key into the sidebar, type a question, and click **Answer**.

## Models

The sidebar offers these Groq models:

- `openai/gpt-oss-20b`
- `openai/gpt-oss-120b`
- `openai/gpt-oss-safeguard-20b` *(a safety-focused preview model, so it may answer general questions oddly)*

> Groq retires models from time to time. If one gives a "model not found" error, check the current list at [console.groq.com/docs/models](https://console.groq.com/docs/models) and update the list in `app.py`.

## Project Structure

```
Que-Ans-Chatbot-Groq
 |-- app.py             the Streamlit app
 |-- requirements.txt   Python packages
 |-- .gitignore         keeps secrets and the venv out of git
 |-- README.md          this file
```

## A note on API keys

Never commit your API key to GitHub. The key is typed into the sidebar and isn't stored anywhere, and `.env` is listed in `.gitignore` to keep it that way.
