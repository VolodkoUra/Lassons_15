def upp(string: str):
    return string.upper()

l = ["adas", "sda", "zsfa"]

r = map(upp, l)

print(next(r))
print(next(r))
print(next(r))