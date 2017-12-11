list_of_chars = "listofcharacters".split()
# builtin function map (faster)
upper_cased = list(map(str.upper, list_of_chars))
print(upper_cased)
print(upper_cased)
# loop (slower)
for c in list_of_chars:
    upper_cased.append(c)
