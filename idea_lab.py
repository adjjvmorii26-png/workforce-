# idea_lab.py
import random

def idea_lab(sandbox, seed_prompt: str = "a sandbox that evolves itself"):
    ideas = [
        f"Autonomous mutation rule based on: '{seed_prompt}'",
        "Dynamic biome shifts during high agent activity",
        "Emergent faction trade protocols",
        "Recursive self-optimization of state ticks"
    ]
    selected_idea = random.choice(ideas)
    sandbox.state["ideas"].append({"prompt": seed_prompt, "generated_idea": selected_idea})
    sandbox.log(f"IdeaLab generated concept: {selected_idea}")
    return selected_idea
