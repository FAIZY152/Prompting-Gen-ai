from fastapi import HTTPException
from src.service import agent_service
from src.models.Agent import Agent

def create_agent_controller(agent: Agent):
    return agent_service.create_agent(agent)

def list_agents_controller():
    return agent_service.list_agents()

def get_agent_controller(agent_id: int):
    agent = agent_service.get_agent(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

def update_agent_controller(agent_id: int, agent: Agent):
    return agent_service.update_agent(agent_id, agent)
