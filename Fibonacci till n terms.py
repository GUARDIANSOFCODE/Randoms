def fibonacci_sequence(n_terms):
    sequence = [0, 1]
    for i in range(2, n_terms):
        next_term = sequence[i-1] + sequence[i-2]
        sequence.append(next_term)
    return sequence[:n_terms]

# Generate Fibonacci sequence with 10 terms
print("Fibonacci Sequence:", fibonacci_sequence(10))
