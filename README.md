# Trace a LangChain App with LangSmith - Social Eagle Week 2 Day 3

A small LangChain app that sends 3 prompts to OpenAI and prints the answers.
LangSmith records every run with zero tracing code in the file - the
environment variables do all of it.

## Setup

```bash
mkdir traced-app && cd traced-app
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create a free LangSmith account at smith.langchain.com and make an API key
(Settings -> API Keys), alongside your OpenAI key.

```bash
export OPENAI_API_KEY="your-openai-key"
export LANGSMITH_TRACING="true"
export LANGSMITH_API_KEY="your-langsmith-key"
export LANGSMITH_PROJECT="caie-week2"
```

(Windows PowerShell: `$env:NAME="value"` for each. `LANGSMITH_*` is the current
naming; older tutorials show `LANGCHAIN_TRACING_V2`.)

## Run

```bash
python traced_app.py
```

Then open smith.langchain.com -> project **caie-week2**. Before hunting the
dashboard, check tracing is actually on: the app prints nothing about tracing,
so the proof is that the runs appear at all. Open one run and expand it to see
the exact prompt sent, the response, latency and token counts.

## Expected finding

Run 3 asks for a 6-step plan and is the expensive one (most tokens, highest
latency); runs 1 and 2 are short. That is visible only because LangSmith puts
tokens and latency side by side.

## Free-tier note

The assignment specifies an OpenAI key. The same file runs on Groq's free
OpenAI-compatible endpoint by setting
`export OPENAI_BASE_URL="https://api.groq.com/openai/v1"` with a Groq key and
changing the model name in the file - LangSmith tracing works unchanged.
