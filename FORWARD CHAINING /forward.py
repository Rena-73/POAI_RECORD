# Knowledge base: list of (conditions, conclusion) rules
knowledge_base = [ 
    (["cough", "fever"], "flu"), 
    (["sore_throat", "runny_nose"], "cold"), 
    (["sore_throat"], "fever")  # Sore throat can lead to fever 
]

# Initial facts
facts = {"cough", "sore_throat"}

# Forward Chaining Function
def forward_chaining():
    inferred = True
    while inferred:
        inferred = False
        for conditions, conclusion in knowledge_base:
            if all(condition in facts for condition in conditions) and conclusion not in facts:
                facts.add(conclusion)
                inferred = True

# Run the inference
forward_chaining()

# Diagnosis
if "flu" in facts:
    print("The patient is diagnosed with flu.")
elif "cold" in facts:
    print("The patient is diagnosed with cold.")
else:
    print("No conclusive diagnosis could be made.")
