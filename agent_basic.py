from agno.agent import Agent
from agno.models.openai import OpenAIChat

# 1) Choose the model (updated syntax)
model = OpenAIChat(
    id="gpt-4o-mini"   # small, fast model
)

# 2) Create the agent with your instruction
assistant = Agent(
    model=model,
    instructions="""
You are a helpful assistant.
Answer questions politely, clearly, and simply.
Keep explanations easy to understand.
"""
)

# 3) Simple chat loop
while True:
    user_input = input("You: ")

    # type 'exit' or 'quit' to stop
    if user_input.lower() in ["exit", "quit"]:
        print("Bye! 👋")
        break

    response = assistant.run(user_input)
    print("Agent:", response)

