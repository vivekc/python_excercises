list_of_chars = "listofcharacters".split()
# builtin function map (faster)
upper_cased = map(str.upper, list_of_chars)
 
# loop (slower)
for c in list_of_chars:
    upper_cased.append(c)
