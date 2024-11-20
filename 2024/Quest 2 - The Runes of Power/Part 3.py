input = """WORDS:ABC

DDDA
DDDB
DDDC
DDDD"""

words, phrase = input.split('\n\n')
_, words = words.split(':')

tracking_set = set()

y = 0
for line in phrase.split('\n'):
    max_x = len(line)
    line += line

    for word in words.split(','):
        for symbol in [word, word[::-1]]:
            for i in [i for i in range(len(line)) if line.startswith(symbol, i)]:
                for x in range(i, i + len(symbol)):
                    if x >= max_x:
                        x -= max_x
                    tracking_set.add((x, y))
    y += 1

    
# vertical
phrase = [''.join(reversed(a)) for a in zip(*phrase.split('\n'))]

y = 0
for line in phrase:
    for word in words.split(','):
        for symbol in [word, word[::-1]]:
            for i in [i for i in range(len(line)) if line.startswith(symbol, i)]:
                for x in range(i, i + len(symbol)):
                    tracking_set.add((y, x))
    y += 1

print(len(tracking_set))