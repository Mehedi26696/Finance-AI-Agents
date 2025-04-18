


from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

# Load environment variables from .env file

load_dotenv()

agent = Agent(
  
     model = Groq(id = "llama-3.3-70b-versatile"),
     tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
     show_tools_calls=True,
     markdown=True,
     instructions = ["Use tables to display data."],
     debug_mode = True,
)

# Run the agent with a prompt

agent.print_response("Summarize and compare analyst recommendations and fundamentals for Tesla and NVIDIA")
