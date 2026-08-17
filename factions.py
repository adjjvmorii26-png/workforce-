# factions.py
import random

def assign_factions(sandbox):
    factions = ["Solaris Legion", "Void Collective", "Verdant Syndicate"]
    sandbox.state["factions"] = {f: [] for f in factions}
    
    for agent in sandbox.state["agents"]:
        assigned = random.choice(factions)
        agent["faction"] = assigned
        sandbox.state["factions"][assigned].append(agent["name"])
    
    sandbox.log("Factions assigned to all active agents.")

def faction_relations(sandbox):
    factions = list(sandbox.state["factions"].keys())
    relations = {}
    for f1 in factions:
        relations[f1] = {}
        for f2 in factions:
            if f1 == f2:
                relations[f1][f2] = "Self"
            else:
                relations[f1][f2] = random.choice(["Allied", "Neutral", "Hostile"])
    sandbox.state["relations"] = relations
    sandbox.log("Faction relation matrix generated.")
