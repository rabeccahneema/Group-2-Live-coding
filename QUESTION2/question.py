programs = [
    {"name": "News", "duration": 1, "type": "news", "reach": 9, "revenue": 1000, "rights": (0, 24)},
    {"name": "Movie", "duration": 2, "type": "entertainment", "reach": 10, "revenue": 5000, "rights": (18, 22)},
    {"name": "Kids Show", "duration": 1, "type": "kids", "reach": 6, "revenue": 800, "rights": (8, 18)},
]

# 24 time slots (1 hour per slot for simplicity)
slots = [None] * 24
prime_time = range(18, 22)

# Sort programs by reach * revenue (weight)
programs.sort(key=lambda p: (p["reach"] * p["revenue"]), reverse=True)

for program in programs:
    start, end = program["rights"]
    for i in range(start, end - program["duration"] + 1):
        if all(slots[j] is None for j in range(i, i + program["duration"])):
            if any(j in prime_time for j in range(i, i + program["duration"])):
                for j in range(i, i + program["duration"]):
                    slots[j] = program["name"]
                break

# Print Schedule
for hour, program in enumerate(slots):
    print(f"{hour}:00 - {hour+1}:00 => {program or 'Free'}")
