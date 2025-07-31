def multiples():
    for a in range(10):
        yield a*3
it = 0
for i in multiples():
    print(f"Iteration {it}: {i}")
    it += 1