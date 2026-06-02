from enum import Enum


class AgentType(str, Enum):
    OPENAI = "openai"
    LANGGRAPH = "langgraph"
    CREWAI = "crewai"
    AUTOGEN = "autogen"
    CUSTOM_API = "custom_api"