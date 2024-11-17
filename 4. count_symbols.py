word = input()

unique_symbols = set(word)

for letter in word:
    unique_symbols.add(letter)

for letter in sorted(unique_symbols):
    print(f"{letter}: {word.count(letter)} time/s")
