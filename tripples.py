import pandas as pd


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_primitive_pythagorean_triples(limit):
    triples = []
    for a in range(1, limit + 1):
        for b in range(a + 1, limit + 1):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c > b and gcd(a, b) == 1:
                triples.append((a, b, int(c)))
    return triples

def main():
    limit = 100
    triples = generate_primitive_pythagorean_triples(limit)

    print("Primitive Pythagorean triples:")
    for triple in triples:
        print(" ".join(map(str, triple)))

    print("\nNumber of primitive Pythagorean triples:", len(triples))

if __name__ == "__main__":
    main()
