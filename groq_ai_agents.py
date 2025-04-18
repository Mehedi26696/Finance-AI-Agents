
from phi.agent import Agent
from phi.model.groq import Groq

from dotenv import load_dotenv

# Load environment variables from .env file

load_dotenv()

agent = Agent(
  
     model = Groq(id = "llama-3.3-70b-versatile")

)

# Run the agent with a prompt

agent.print_response("Write 10 football player names")

agent.print_response("Write a story about a cat")

