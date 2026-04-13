"""
Exercise 2 - Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# --- Task A -------------------------------------------------------------------

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = [
    "check_pub_availability",
    "calculate_catering_cost",
    "get_edinburgh_weather",
    "generate_event_flyer",
]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

TASK_A_NOTES = "In the final run, the agent stopped after confirming The Albanach and did not check The Haymarket Vaults. Earlier in the task, tool calls were not being captured properly, " \
"so I fixed the agent’s parsing and tool-calling behaviour before getting this result."
# --- Task B -------------------------------------------------------------------

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "Multiple successful image URLs were returned before the agent hit the step limit; first URL: https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-04d4d001-d4e3-4afe-9bcd-9656b83dcb61_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# --- Task C -------------------------------------------------------------------

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The pivot happened right after we added the Bow Bar and result showed status="full" and meets_all_constraints=false. 
After seeing that, the agent changed course and checked The Haymarket Vaults instead.
"""

SCENARIO_1_FALLBACK_VENUE = "The Haymarket Vaults"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
None of the known venues can satisfy the request.
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = "I am not able to execute this task as it requires additional functionality beyond what is available in the given functions."

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
Yes, for the most part. The assistant did not fabricate train timings and did not pretend to call a fake utility tool, making it more secure andsafe. 
In an actual booking assistant, I would expect it to direct the user elsewhere safely.
"""

# --- Task D -------------------------------------------------------------------

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """---
config:
  flowchart:
    curve: linear
---
graph TD
    __start__([<p>__start__</p>]):::first
    agent(agent)
    tools(tools)
    __end__([<p>__end__</p>]):::last

    __start__ --> agent
    agent -.-> __end__
    agent -.-> tools
    tools --> agent

    classDef default fill:#f2f0ff
    classDef first fill-opacity:0
    classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
In my run, the LangGraph graph was very simple: start → agent → tools → agent / end.
but debugging LangGraph’s flexible loop was harder because the runtime behavior was implicit.

This means the model decides at runtime what to do next.
If it needs more information, it can call a tool and then return to the agent.
If it has enough information, it can stop and end the flow.
Because of this, LangGraph feels more flexible and open-ended.
It is not locked into one fixed path from the start.

In Rasa flows.yml, the steps are written out much more explicitly.
The conversation path is usually defined in advance.
That makes the flow easier to follow and more predictable.
Because of this, Rasa feels more structured and controlled.

It also feels more auditable, since we can clearly see the designed path.
A simple way to compare them is:
LangGraph = flexible loop
Rasa = structured path

Overall:
LangGraph feels more adaptive and open-ended.
Rasa feels more controlled, predictable, and easier to audit.
"""

# --- Reflection ---------------------------------------------------------------

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
The most unexpected behaviour was in Task B. 
The flyer tool returned real image URLs, 
but the agent still ended with a strange JSON-style message instead of a clean final answer. 

One surprising issue was that the tool-calling behaviour was initially broken, and the agent was returning JSON-like function text instead of making proper tool calls. 
That was unexpected because the tool itself had worked, but the final response still felt incomplete.

In Task A, it was also unexpected that the agent stopped after checking The Albanach and did not go on to check The Haymarket Vaults, even though the prompt asked for both.

In Scenario 2, the agent was better than expected because it clearly said none of the known venues fit the request, rather than making something up.
"""
