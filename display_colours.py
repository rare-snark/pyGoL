from blessings import Terminal

t = Terminal()

print(f"number of colours: {t.number_of_colors}")

for i in range(0, t.number_of_colors+1):
    print(t.normal + str(i) + t.color(i) + "    the quick brown fox jumps over the lazy dog")