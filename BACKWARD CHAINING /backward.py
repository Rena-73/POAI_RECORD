# Knowledge Base (Rules in IF-THEN format)
knowledge_base = {
    "flu": [["cough", "fever"]],
    "fever": [["sore_throat"]],
}

# Known facts
facts = {"sore_throat", "cough"}

# Backward chaining function
def backward_chaining(goal):
    if goal in facts:
        return True
    if goal in knowledge_base:
        for conditions in knowledge_base[goal]:
            if all(backward_chaining(cond) for cond in conditions):
                return True
    return False

# Query: Does the patient have flu?
query = "flu"
if backward_chaining(query):
    print(f"The patient is diagnosed with {query}.")
else:
    print(f"The patient does NOT have {query}.")
