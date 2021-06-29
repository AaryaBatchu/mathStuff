import random

# graph is [0, 0] to [5, 5]
times = 1000000
total_count = []
total = 0

for i in range(times):
    ball = [random.randrange(6), random.randrange(6)]

    count = 0
    possibilities = [[i, j] for i in range(6) for j in range(6)]

    while True:
        count += 1

        roll = [random.randrange(6), random.randrange(6)]
        if roll == ball:
            break
        if roll[0] < ball[0]:
            for possibility in possibilities:
                if possibility[0] <= roll[0]:
                    possibilities.pop(possibilities.index(possibility))
        elif roll[0] > ball[0]:
            for possibility in possibilities:
                if possibility[0] >= roll[0]:
                    possibilities.pop(possibilities.index(possibility))
        elif roll[0] == ball[0]:
            for possibility in possibilities:
                if possibility[0] != roll[0]:
                    possibilities.pop(possibilities.index(possibility))
        if roll[1] < ball[1]:
            for possibility in possibilities:
                if possibility[1] <= roll[1]:
                    possibilities.pop(possibilities.index(possibility))
        elif roll[1] > ball[1]:
            for possibility in possibilities:
                if possibility[1] >= roll[1]:
                    possibilities.pop(possibilities.index(possibility))
        elif roll[1] == ball[1]:
            for possibility in possibilities:
                if possibility[1] != roll[1]:
                    possibilities.pop(possibilities.index(possibility))

        guess = random.choice(possibilities)
        if guess == ball:
            break

    total_count.append(count)
    total += count

mean = float(total / times)
variance = 0.0
for count in total_count:
    variance += (mean - count) ** 2
variance /= times

print("x̄: %f\nμ: %f" % (mean, (variance ** 0.5)))
