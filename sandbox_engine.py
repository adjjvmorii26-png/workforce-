# sandbox_engine.py
import datetime

class Sandbox:
    def __init__(self):
        self.state = {
            "world": {},
            "agents": [],
            "map": [],
            "factions": {},
            "relations": {},
            "quests": [],
            "events": [],
            "logs": [],
            "dashboard": {},
            "ideas": []
        }

    def log(self, message: str):
        entry = f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {message}"
        self.state["logs"].append(entry)

    def run_module(self, module_func, *args, **kwargs):
        module_name = getattr(module_func, '__name__', str(module_func))
        self.log(f"Executing module: {module_name}")
        result = module_func(self, *args, **kwargs)
        return result
