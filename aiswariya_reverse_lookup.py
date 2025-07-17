scores = {
    "Anita": 92,
    "Ravi": 85,
    "Kiran": 76,
    "Zoya": 88
}

value = int(input("Enter score: "))
# Create a reverse dictionary: score → name
reverse = dict(zip(scores.values(), scores.keys()))
print(reverse.get(value, "Not found"))