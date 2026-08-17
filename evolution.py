# evolution.py
def evolve_agents(sandbox):
    for agent in sandbox.state["agents"]:
        agent["xp"] += 50
        if agent["xp"] >= 50:
            agent["level"] += 1
            agent["hp"] += 10
            sandbox.log(f"Agent {agent['name']} leveled up to Lvl {agent['level']}!")
