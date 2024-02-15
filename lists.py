users = ["geg", "dhdh", "jfjd"]

data = [1, "geg", True]

emptylist = []

print("geg" in emptylist)
print(users[-1])
print(data.index("geg"))
print(data.index(1))
print(data[1:])

print(len(data))

data += ["alma"]

print(data)

mytuple = (1, 4, 7, 8, 11, 15)
(one, *two, three, four) = mytuple
print(one)
print(two)
print(three)
print(four)