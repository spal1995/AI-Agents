from crewai import Task
from agents import video_researcher, video_writer
from tools import youtube_channel_tool

# Research Task
research_task = Task(
    description="Identify the video:{topic}.Research and get the information from the video.",
    agent=video_researcher,
    tools=[youtube_channel_tool],
    expected_output="Researcher will provide 3 paragraph report about the video for the topic:{topic} from the youtube channel"
)


# Writing Task
writing_task = Task(
    description="Get the information from the video: {topic}.Write a blog about the video.",
    agent=video_writer,
    tools=[youtube_channel_tool],
    expected_output="Summarize the information to a blog style about the video for the topic:{topic}",
    async_execution=False,
    output_file="blog_for_video.md"
)