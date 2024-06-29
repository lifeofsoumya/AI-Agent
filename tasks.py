from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# Task on researching about my video

research_task = Task(
    description=(
        "identify the video {topic}", 
        "Get detailed information about the video from channel"
    ),
    expected_output="An educational tech blog based on the {topic} of the video content",
    tools=[yt_tool],
    agent=blog_researcher
)

writing_task = Task(
    description=(
        "get the info from the youtube channel on topic {topic}",
    ),
    expected_output="summerize the info from the youtube channel video on the topic {topic} and create the content of the blog",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='blog.md'
)