import math

def calculate_shannon_entropy(data: str) -> float:
    """Calculates the Shannon entropy of a string."""
    if not data:
        return 0
    entropy = 0
    for x in set(data):
        p_x = data.count(x) / len(data)
        entropy += - p_x * math.log2(p_x)
    return entropy
