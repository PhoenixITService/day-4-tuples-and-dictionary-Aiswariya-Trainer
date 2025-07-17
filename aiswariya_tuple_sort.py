import operator

data = [
    ('A', 1, 2),
    ('B', 3),
    ('C', 4, 5, 6),
    ('D',),
    ('E', 7, 8)
]

res1 = (list(
    map(
        operator.itemgetter(0),
        sorted(
            data,
            key=len
        )
    )
))

print(res1)