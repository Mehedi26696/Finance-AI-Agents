
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.playground import Playground, serve_playground_app


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

 

app = Playground(agents=[finance_agent, web_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)