# quests.py
def quests(sandbox):
    generated_quests = [
        {"title": "Explore the Rift", "reward_xp": 100, "status": "Available"},
        {"title": "Secure Trade Route", "reward_xp": 150, "status": "In Progress"}
    ]
    sandbox.state["quests"].extend(generated_quests)
    sandbox.log(f"Quests module registered {len(generated_quests)} new missions.")
