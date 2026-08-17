# world_events.py
import random

def world_events(sandbox):
    events_pool = [
        "Mana Storm over Sector 4",
        "Dimensional Rift opened",
        "Resource Surge detected in northern biome",
        "Ancient Ruins discovered"
    ]
    event = random.choice(events_pool)
    sandbox.state["events"].append(event)
    sandbox.log(f"WorldEvent triggered: {event}")
