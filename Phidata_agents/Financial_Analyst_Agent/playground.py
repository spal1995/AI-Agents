from phi.playground import Playground, serve_playground_app
from financial_agent import multi_agent

app = Playground(
    agents=[multi_agent]
    #title="Financial Analysis Assistant",
    #description="AI-powered stock analysis and market insights"
).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)e