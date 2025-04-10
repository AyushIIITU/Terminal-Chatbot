# Terminal Chatbot

## 🧠 AI Shell Agent

An AI-powered command line agent that converts natural language instructions into executable shell commands using the `granite3.2:8b` LLM locally with [Ollama](https://ollama.com/).
```bash
ollama run granite3.2
```
---

## 🚀 Features

- Converts your plain English tasks into actionable shell commands.
- Interactively approves and executes them.
- Fully local & private with no internet-based LLMs.

---

## 📦 Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed
---

## 🛠️ Setup

### 1. Clone this repo

```bash
git clone https://github.com/your-username/ai-shell-agent.git
cd ai-shell-agent
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```


## ▶️ Run the Agent

Once everything is ready:

```bash
python client.py
```

You’ll be prompted like:

```
🧠 Task for AI Agent (or 'q' to quit):
> create a new git repo and push it to GitHub
```

The model will generate and show you the commands. Approve them to execute:

```
✅ Approve? (y/n): y
```

---

## ⚠️ Warnings

- Be cautious with tasks — always read generated commands before approving.
- Make sure you run this in a safe terminal environment.
