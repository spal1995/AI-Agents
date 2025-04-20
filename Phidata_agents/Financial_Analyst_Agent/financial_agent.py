from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv
load_dotenv()

import os
os.environ["PHI_API_KEY"] = os.getenv("PHI_API_KEY")
#os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

finance_agent = Agent(
    name="Finance Agent",
    role="Analyze stocks and provide financial recommendations",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, 
                         analyst_recommendations=True, 
                         company_info=True, 
                         company_news=True,
                         technical_indicators=True,
                         stock_fundamentals=True)],
    instructions=[
        "Present data in organized tables",
        "Provide both technical and fundamental analysis",
        "Include risk factors in recommendations"
    ]
)

web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for latest financial news and information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=[
        "Always include sources in your response",
        "Focus on financial news and market analysis",
        "Provide recent and relevant information"
    ]
)

multi_agent = Agent(
    name="Financial Assistant",
    model=OpenAIChat(id="gpt-4o"),
    team=[web_search_agent, finance_agent],
    instructions=[
        "Combine web information with financial data",
        "Provide comprehensive analysis",
        "Present information in a clear, structured format",
        "Always include both technical and fundamental factors"
    ],
    markdown=True,
    show_tool_calls=True,
    add_history_to_messages=True
)