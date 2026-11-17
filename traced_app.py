"""
Trace a LangChain App with LangSmith - Social Eagle Week 2 Day 3.

Nothing in this file mentions LangSmith. Tracing is switched on entirely by
environment variables - that is the lesson:

    export OPENAI_API_KEY="your-openai-key"
    export LANGSMITH_TRACING="true"
    export LANGSMITH_API_KEY="your-langsmith-key"
    export LANGSMITH_PROJECT="caie-week2"

Runs land in the "caie-week2" project at smith.langchain.com - open one run
to see the exact prompt sent, the response, latency and token counts.
"""

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "Explain what an API is to a 10-year-old in 3 sentences.",
    "Give me a 4-line professional WhatsApp message asking a client for a pending invoice payment.",
    "Write a detailed 6-step plan to learn Python in 30 days, with weekly milestones.",
]

for i, prompt in enumerate(prompts, start=1):
    answer = llm.invoke(prompt)
    print(f"--- Prompt {i}: {prompt}")
    print(answer.content)
    print()

# The third prompt asks for much more output than the first two. When the runs
# appear in LangSmith, compare token counts side by side - run 3 should be the
# expensive one, and for a good reason.
