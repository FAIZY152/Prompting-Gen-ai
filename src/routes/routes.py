from fastapi import APIRouter, HTTPException
from src.models.Agent import Agent   # import the class, not the module
from src.controller import AgentController

router = APIRouter()

@router.post("/")
def create_agent(agent: Agent):
    return AgentController.create_agent_controller(agent)

@router.get("/")
def list_agents():
    
    return AgentController.list_agents_controller()

@router.get("/{agent_id}")
def get_agent(agent_id: int):
    return AgentController.get_agent_controller(agent_id)
