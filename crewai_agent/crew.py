from crewai  import Crew,Process
from agents import video_researcher, video_writer
from tasks import research_task, writing_task

crew = Crew(
    name="Research and Writing Crew",
    description="A crew of agents working together to research and write about a topic from the Youtube channel.",
    tasks=[research_task, writing_task],
    agents=[video_researcher, video_writer],
    process=Process.sequential,
    memory=True,
    max_rpm=100,
    cache=True,
    share_crew=True
)

# Run the crew
result = crew.kickoff(inputs={"topic":"2.0 Live Agentic AI And Generative AI With Cloud Bootcamp Batch Announcement"})
print(result)
