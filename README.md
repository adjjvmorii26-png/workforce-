sandbox/
├── main_hub.py          # Unified entry point & external hub interface
├── sandbox_engine.py    # Core state manager & execution logger
├── idea_lab.py          # Stochastic feature & concept generator
├── world_builder.py     # World parameters & environment setup
├── self_debugger.py     # Cognitive refactoring & execution log resolution
├── multi_agent.py       # Agent instantiation & interaction logic
├── factions.py          # Faction assignment & relationship matrix
├── evolution.py         # XP, leveling, & stats progression
├── world_events.py      # Dynamic event generation system
├── quests.py            # Procedural quest registry
├── world_map.py         # 2D grid terrain map builder
├── dashboard.py         # Engine state telemetry & statistics
├── raw_export.py        # Normalized JSON data exporter
└── realtime.py          # High-frequency tick update loop
# workforce-

ModuleResponsibilitiesKey Functions
sandbox_engineCentralized state container & execution loggerSandbox.run_module()
main_hubOrchestrates pipeline initialization & exportsMainHub.load_all(), MainHub.get_raw()
multi_agentSpawns agents & simulates cross-agent behaviormulti_agent_module(), agent_interactions()
factionsManages factions and alignment matricesassign_factions(), faction_relations()
world_mapBuilds procedural N \times M terrain gridworld_map()
evolutionCalculates XP gains & level incrementsevolve_agents()
raw_exportFlattens state into a normalized JSON dictionaryexport_raw()
realtimeHandles per-tick spatial movement & updatesrealtime_updates()



from main_hub import MainHub

# Initialize the Sandbox Hub
hub = MainHub()

# Execute full engine initialization sequence
hub.load_all()

# Retrieve normalized raw state dump
raw_data = hub.get_raw()
print(f"Loaded {len(raw_data['agents'])} agents into {raw_data['world']['name']}")

# Run a real-time tick update
hub.start_realtime()



