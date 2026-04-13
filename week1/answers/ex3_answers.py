"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  Hi, I'm calling to confirm tonight's booking.
How many guests are you confirming for tonight's event?
Your input ->  We're expecting 160 guests.
And how many of those guests will need vegan meals?
Your input ->  About 50 of them need vegan meals.
Ok, I am updating guest_count to 160 respectively.
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  The deposit would be 200.
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  Hi, I am calling to confirm tonight's booking.
How many guests are you confirming for tonight's event?
Your input ->  We're expecting 160 guests.


And how many of those guests will need vegan meals?
Your input ->  Around 160
Ok, I am updating guest_count to 160 respectively.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
Your input ->  no wait I want 50 vegan options
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  The deposit would be 500.
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON = "a deposit of £500 exceeds the organiser's authorised limit of £300 so the issue was escalated as expected"
   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Is there anything else I can help you with?
Your input ->  Hi, I'm calling to confirm tonight's booking.


How many guests are you confirming for tonight's event?
Your input ->  We're expecting 160 guests.



And how many of those guests will need vegan meals?
Your input ->  Can you arrange parking for the speakers?
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
Your input ->  no

I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Okay, stopping confirm_booking.
Is there anything else I can help you with?
Your input ->  no thank you

I'm sorry, I'm not trained to help with that.
Okay, I'll be around in case you need further help.
? How would you rate your experience today? (Use arrow keys)
 » 1: 👍 Satisfied (/SetSlots(csat_score=satisfied))
   2: 👎 Not Satisfied (/SetSlots(csat_score=unsatisfied))
   Type out your own message...
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
After I asked about parking, the agent treated it as out of scope and said it was not trained to help with that. 

It then reminded me it only handles booking confirmation and asked whether I wanted to continue the booking flow. 

When I said no, it stopped the flow cleanly and asked for feedback how it performed.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
LangGraph gave a broad refusal based on missing capability.

Rasa CALM handled it more like a structured employee: reject the off-topic request, restate scope, and steer the conversation back to the allowed flow.

Both avoided making something up, but CALM felt more controlled and auditable.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I first uncommented the cutoff guard in actions.py
Because the real system time was before 16:45, I temporarily changed the condition to match the current machine time
Then I retrained with uv run rasa train
I restarted the action server
I ran a normal happy-path booking in rasa shell
instead of confirming, the bot escalated with the “past 16:45 / before the 5 PM deadline” message
then I changed the condition back to the original 16:45 rule
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.


CALM_VS_OLD_RASA = """
The main gain with CALM is that the LLM now handles the natural language side for us.

Inputs like “about 160 guests” can be understood and mapped into slots without writing regex-heavy validation code. 
It also reduces some of the manual setup compared with old Rasa, because there is less intent and rule wiring to maintain.

The cost is that part of the behaviour is now model-driven, so it feels a little less explicit and predictable than a fully hand-written rules approach. 

What I still trust most is the Python action layer, because the hard business limits are enforced there: guest count, deposit, vegan ratio, and the cutoff time. 
That deterministic part is what makes it safer for real booking decisions.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
CALM took more setup than LangGraph because I needed config files, training, two terminals, and a licence before I could test anything. 
What that extra setup gave me was more control. 

The agent stayed inside the booking flow, did not improvise much, and could not use tools outside the defined flow. 
For this kind of confirmation task, I think that is mostly a feature, because being strict is safer than being creative.
"""
