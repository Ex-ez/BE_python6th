s = "Hello World    "

print(s.replace("world".title(), "there"))
split_str = s.split(",")
print(split_str)
print("".join(split_str))

print(s.startswith("Hello"))