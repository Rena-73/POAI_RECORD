
def unify(x, y, theta={}):
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x.islower():
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.islower():
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

def resolution(kb, query):
    for clause in kb:
        head = clause[-1]
        theta = unify(head, query, {})
        if theta is not None:
            if len(clause) == 1:
                return True  # It’s a fact
            # Resolve all premises in the body
            body = clause[:-1]
            if all(resolution(kb, substitute(b, theta)) for b in body):
                return True
    return False

def substitute(expr, theta):
    if isinstance(expr, list):
        return [theta.get(x, x) for x in expr]
    else:
        return theta.get(expr, expr)

# Knowledge base:
# If Human(John), then Mortal(John)
# Fact: Human(John)

knowledge_base = [
    [["Human", "John"]],                     # Fact
    [["Human", "x"], ["Mortal", "x"]],       # Rule: Human(x) => Mortal(x)
]

query = ["Mortal", "John"]

if resolution(knowledge_base, query):
    print("Query is resolved: John is Mortal")
else:
    print("Query could not be resolved")
