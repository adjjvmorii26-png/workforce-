# dashboard.py
def dashboard(sandbox):
    sandbox.state["dashboard"] = {
        "total_agents": len(sandbox.state["agents"]),
        "total_factions": len(sandbox.state["factions"]),
        "active_quests": len(sandbox.state["quests"]),
        "recent_events": len(sandbox.state["events"]),
        "status": "Healthy / Operational"
    }
    sandbox.log("Dashboard analytics updated.")
