# tests/test_sandbox.py

import pytest
from sandbox_engine import Sandbox
from idea_lab import idea_lab
from world_builder import world_builder
from self_debugger import self_debugger
from multi_agent import multi_agent_module, agent_interactions
from factions import assign_factions, faction_relations
from evolution import evolve_agents
from world_events import world_events
from quests import quests
from world_map import world_map
from dashboard import dashboard
from raw_export import export_raw
from realtime import realtime_updates
from main_hub import MainHub


@pytest.fixture
def sandbox():
    """Provides a fresh, empty Sandbox instance for isolated tests."""
    return Sandbox()


@pytest.fixture
def initialized_hub():
    """Provides a fully initialized MainHub instance with all modules loaded."""
    hub = MainHub()
    hub.load_all()
    return hub


# --- 1. Core Sandbox Engine ---
def test_sandbox_engine_initialization(sandbox):
    assert isinstance(sandbox.state, dict)
    assert "agents" in sandbox.state
    assert "logs" in sandbox.state
    assert len(sandbox.state["logs"]) == 0


def test_sandbox_run_module(sandbox):
    def dummy_module(sb, text):
        sb.state["test_key"] = text
        return f"result: {text}"

    result = sandbox.run_module(dummy_module, "hello")
    assert result == "result: hello"
    assert sandbox.state["test_key"] == "hello"
    assert len(sandbox.state["logs"]) == 1
    assert "Executing module: dummy_module" in sandbox.state["logs"][0]


# --- 2. Idea Lab ---
def test_idea_lab(sandbox):
    prompt = "autonomous evolution"
    idea = sandbox.run_module(idea_lab, seed_prompt=prompt)
    assert isinstance(idea, str)
    assert len(sandbox.state["ideas"]) == 1
    assert sandbox.state["ideas"][0]["prompt"] == prompt


# --- 3. World Builder ---
def test_world_builder(sandbox):
    sandbox.run_module(world_builder)
    world = sandbox.state["world"]
    assert world["name"] == "Aetheria-Prime"
    assert world["dimensions"]["width"] == 10
    assert world["dimensions"]["height"] == 10


# --- 4. Self Debugger ---
def test_self_debugger(sandbox):
    friction = "High latency in multi-agent routing"
    result = sandbox.run_module(self_debugger, friction_point=friction)
    assert friction in result
    assert any("[Cognitive Refactor]" in log for log in sandbox.state["logs"])


# --- 5. Multi Agent System ---
def test_multi_agent_spawn_and_interact(sandbox):
    agent_names = ["Nexus", "Aegis"]
    sandbox.run_module(multi_agent_module, agent_names)
    assert len(sandbox.state["agents"]) == 2
    assert sandbox.state["agents"][0]["name"] == "Nexus"

    interactions = sandbox.run_module(agent_interactions)
    assert isinstance(interactions, list)
    assert len(interactions) == 1


# --- 6. Factions & Relations ---
def test_factions_assignment_and_relations(sandbox):
    sandbox.run_module(multi_agent_module, ["Agent_1", "Agent_2"])
    sandbox.run_module(assign_factions)

    assert len(sandbox.state["factions"]) == 3
    assert all(agent["faction"] is not None for agent in sandbox.state["agents"])

    sandbox.run_module(faction_relations)
    relations = sandbox.state["relations"]
    assert "Solaris Legion" in relations
    assert relations["Solaris Legion"]["Solaris Legion"] == "Self"


# --- 7. Evolution ---
def test_evolve_agents(sandbox):
    sandbox.run_module(multi_agent_module, ["Evolver"])
    initial_level = sandbox.state["agents"][0]["level"]
    initial_hp = sandbox.state["agents"][0]["hp"]

    sandbox.run_module(evolve_agents)

    updated_agent = sandbox.state["agents"][0]
    assert updated_agent["level"] == initial_level + 1
    assert updated_agent["hp"] == initial_hp + 10


# --- 8. World Events ---
def test_world_events(sandbox):
    sandbox.run_module(world_events)
    assert len(sandbox.state["events"]) == 1
    assert isinstance(sandbox.state["events"][0], str)


# --- 9. Quests ---
def test_quests_registration(sandbox):
    sandbox.run_module(quests)
    assert len(sandbox.state["quests"]) == 2
    assert sandbox.state["quests"][0]["status"] == "Available"


# --- 10. World Map ---
def test_world_map_grid_generation(sandbox):
    sandbox.run_module(world_builder)
    sandbox.run_module(world_map)
    grid = sandbox.state["map"]

    assert len(grid) == 10
    assert len(grid[0]) == 10
    assert grid[0][0] in ["Plains", "Forest", "Mountain", "Desert", "Water"]


# --- 11. Dashboard ---
def test_dashboard_metrics(sandbox):
    sandbox.run_module(multi_agent_module, ["A1", "A2"])
    sandbox.run_module(dashboard)

    metrics = sandbox.state["dashboard"]
    assert metrics["total_agents"] == 2
    assert metrics["status"] == "Healthy / Operational"


# --- 12. Raw Export ---
def test_raw_export(sandbox):
    sandbox.run_module(world_builder)
    exported = export_raw(sandbox)

    assert "world" in exported
    assert "agents" in exported
    assert "timestamp" in exported
    assert exported["world"]["name"] == "Aetheria-Prime"


# --- 13. Realtime Update Loop ---
def test_realtime_updates(sandbox):
    sandbox.run_module(multi_agent_module, ["Runner"])
    agents = realtime_updates(sandbox)

    agent = agents[0]
    assert 0 <= agent["x"] <= 9
    assert 0 <= agent["y"] <= 9


# --- 14. Main Hub Integration Test ---
def test_main_hub_full_pipeline(initialized_hub):
    raw_data = initialized_hub.get_raw()

    assert raw_data["world"]["name"] == "Aetheria-Prime"
    assert len(raw_data["agents"]) == 4
    assert len(raw_data["map"]) == 10
    assert raw_data["dashboard"]["status"] == "Healthy / Operational"
