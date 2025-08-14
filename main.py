# run_mistral_agent.py
import asyncio
from dotenv import load_dotenv
load_dotenv()

# LangChain Mistral chat model
from langchain_mistralai import ChatMistralAI

# Browser-Use
from browser_use import Agent

async def main():
    # create a Mistral-backed chat model (uses MISTRAL_API_KEY from env)
    llm = ChatMistralAI(
        model="mistral-large-latest",   # pick the Mistral model you want
        temperature=0.0,
        max_retries=2,
    )

    # create an Agent (task = what you want the agent to do)
    agent = Agent(
        task="Open example.com and find the main contact email, then summarize it.",
        llm=llm,
        use_vision=True,    # enable screenshots/vision if you want
        # browser settings (optional)
        # browser_args={"headless": False}
    )

    # run the agent (it will launch a browser and run)
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
