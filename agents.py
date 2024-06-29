from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"

#content researcher 

blog_researcher = Agent(
    role="Blog researcher from youtube videos", 
    goal="Get the relevnt video content for the topic {topic} from youtube channel",
    name="Senior blog researcher",
    verbose=True,
    memory=True,
    llm=llm,
    backstory=(
        "Expert in understanding videos on ReactJS, NodeJS, DevOps, full stack applications"
    ),
    tools=[yt_tool],
    allow_delegation=True
)

# blog writer agent

blog_writer = Agent(
    role="Blog writer", 
    goal="Elaborate tech topics about youtube video on {topic}",
    name="Senior blog writer",
    verbose=True,
    memory=True,
    llm=llm,
    backstory=(
        "Expert in ReactJS, NodeJS, Javascript, devops",
        "Good with educational technical content"
    ),
    tools=[yt_tool ],
    allow_delegation=False
)