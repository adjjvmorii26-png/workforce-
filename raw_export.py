# raw_export.py
import datetime

def export_raw(sandbox):
    return {
        "world": sandbox.state.get("world", {}),
        "agents": sandbox.state.get("agents", []),
        "map": sandbox.state.get("map", []),
        "factions": sandbox.state.get("factions", {}),
        "relations": sandbox.state.get("relations", {}),
        "quests": sandbox.state.get("quests", []),
        "events": sandbox.state.get("events", []),
        "dashboard": sandbox.state.get("dashboard", {}),
        "logs": sandbox.state.get("logs", []),
        "timestamp": datetime.datetime.now().isoformat()
    }
