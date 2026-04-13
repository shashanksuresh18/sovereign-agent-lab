"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Albanach"
QUERY_1_VENUE_ADDRESS = "2 Hunter Square, Edinburgh"
QUERY_2_FINAL_ANSWER  = "No venue is available for 300 people with vegan options."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
I only changed sovereign_agent/tools/mcp_venue_server.py by marking The Albanach as full, then reran the client. 

After that, Query 1 changed from The Albanach to The Haymarket Vaults, but the discovered tools and Query 2 stayed the same. 
I did not need to update the client logic for the venue data change itself, which shows the MCP server acts like a shared tool layer.
"""


# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 233   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 191   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP gives more than file separation. It creates a shared tool interface that different clients can connect to and discover dynamically. 
In my run, changing the venue data on the server changed the agent’s answer without needing a client-side rewrite. 
That makes it easier to reuse the same business capabilities across both the research agent and the confirmation side.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- The LangGraph research agent handles open-ended venue research because it can choose tools, compare options, and adapt when a venue is full.

- The Rasa CALM booking agent handles the manager call because it follows a strict flow and applies deterministic business rules before confirming anything.

- The MCP venue server acts as the shared tool layer so both agents can use the same venue data and tool interface without duplicating logic.

- A memory layer stores useful project context and past decisions so the research side does not need to rediscover the same information every time.

- An observability and guardrail layer tracks tool calls, failures, and costs so the full system is easier to monitor and safer to run in production."""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The research part should be handled by the LangGraph agent, while the manager call should be handled by the Rasa CALM agent. 
In my runs, the LangGraph side was better for open-ended work because it could search venues, fetch details, and change its answer when the MCP server data changed. 
The Rasa side felt better for the confirmation call because it followed a strict flow, confirmed the happy-path booking, escalated when the deposit was too high, and handled the parking question by keeping the conversation inside scope. 
Swapping them feels wrong because the research side needs flexibility, but the phone call needs control and clear business rules.
"""

