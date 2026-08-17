# self_debugger.py
def self_debugger(sandbox, friction_point: str = "I can't think creatively"):
    resolution = f"Refactored cognitive bottleneck '{friction_point}' into stochastic decision trees."
    sandbox.state["logs"].append(f"[Cognitive Refactor] {resolution}")
    sandbox.log(f"SelfDebugger resolved: {friction_point}")
    return resolution
