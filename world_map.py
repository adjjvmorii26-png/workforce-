# world_map.py
import random

def world_map(sandbox):
    terrains = ["Plains", "Forest", "Mountain", "Desert", "Water"]
    w = sandbox.state["world"].get("dimensions", {}).get("width", 5)
    h = sandbox.state["world"].get("dimensions", {}).get("height", 5)
    
    grid = [[random.choice(terrains) for _ in range(w)] for _ in range(h)]
    sandbox.state["map"] = grid
    sandbox.log(f"WorldMap generated a {w}x{h} tile grid.")
