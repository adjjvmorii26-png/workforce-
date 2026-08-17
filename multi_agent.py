# multi_agent.py
import random

def multi_agent_module(sandbox, agent_names: list):
    for name in agent_names:
        agent = {
            "id": name.lower().replace(" ", "_"),
            "name": name,
            "hp": 100,
            "level": 1,
            "xp": 0,
            "x": random.randint(0, 9),
            "y": random.randint(0, 9),
            "faction": None,
            "status": "Active"
        }
        sandbox.state["agents"].append(agent)
    sandbox.log(f"MultiAgent initialized {len(agent_names)} agents.")

def agent_interactions(sandbox):
    agents = sandbox.state["agents"]
    interactions = []
    if len(agents) >= 2:
        a1, a2 = random.sample(agents, 2)
        interaction_type = random.choice(["shared data with", "sparred with", "formed pact with"])
        log_msg = f"Agent {a1['name']} {interaction_type} {a2['name']}"
        interactions.append(log_msg)
        sandbox.log(log_msg)
    return interactions
