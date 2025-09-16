from src.models.Agent import Agent

# Fake in-memory DB
agents_db: list[Agent] = []

def create_agent(agent: Agent):
    agents_db.append(agent)
    return {"message": f"Agent {agent.name} created successfully"}

def list_agents():
    return agents_db

def get_agent(agent_id: int):
    try:
        return agents_db[agent_id] if 0 <= agent_id < len(agents_db) else None
    except IndexError:
        return None
