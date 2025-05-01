from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Web Agent using DuckDuckGo
web_agent = Agent(
    name="web_agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    show_tools_calls=True,
    markdown=True,
    instructions=["Always include the source of the information."]
)

# Finance Agent using Yahoo Finance
finance_agent = Agent(
    name="finance_agent",
    role="Get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_info=True
    )],
    show_tools_calls=True,
    markdown=True,
    instructions=["Use tables to display data."]
)

# Team Agent that delegates
agent_team = Agent(
    team=[web_agent, finance_agent],
     model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Always include the source of the information.",
        "Use tables to display data."
    ],
    show_tools_calls=True,
    markdown=True
)

# Run the team on a query
agent_team.print_response("Summarize and compare analyst recommendations and share the latest news for Tesla and NVIDIA")
 

