"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER = "The Haymarket Vaults"
PART_A_XML_ANSWER = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT = True  # True or False
PART_A_XML_CORRECT = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
All three formats returned a correct answer on the clean dataset. 
The plain version chose The Haymarket Vaults, while the XML and sandwich versions chose The Albanach. 
Formatting changed which valid venue the model preferred, but it did not cause an error. 
That suggests the task was simple enough that the stronger model could solve it reliably in a very presentation style.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER = "The Haymarket Vaults"
PART_B_XML_ANSWER = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT = True
PART_B_XML_CORRECT = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The Holyrood Arms was the hardest distractor because it satisfied the capacity and vegan requirements, so it looked nearly correct. 
Its only failing detail was status=full.
A model that skimmed instead of checking every constraint could easily choose it by mistake, shows model was powerful enough to distinguish.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True  # True or False

PART_C_PLAIN_ANSWER = "The Haymarket Vaults"
PART_C_XML_ANSWER = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C ran because Parts A and B were fully correct, so the benchmark switched to the smaller 8B model to try to expose a formatting weakness.
The smaller model also answered all three conditions correctly.
In this run, formatting did not create a failure, which suggests the dataset was still short and clear enough for both models.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the prompt is long or messy,
when near-miss distractors sit close to the correct answer, when the answer is buried among similar choices, and when the model is weaker or more likely to skim.
This experiment shows, structure such as XML tags or repeating the question can help the model stay focused on the right constraints. 

In this run, the effect was limited because the dataset was simple and both models handled itvery well.
One observation Part A used less tokens compared to Part B and C, which may have contributed to the model's performance.
"""
