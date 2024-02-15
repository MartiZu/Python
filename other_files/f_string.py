person = "Dave"
coins = 3
print("\n" + person + " has " + str(coins) + " coins left.")

#old string ways
message = "\n%s has %s coins left." %(person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{0} has {1} coins left.".format(person, coins)
print(message)

message = "\n{person} has {coins} coins left.".format(person=person, coins=coins)
print(message)

player = { 'person': 'Martina', 'coins': 4}

message = "\n{person} has {coins} coins left.".format(**player)
print(message)

message2 = f"\n{person} has {coins} coins left"
print(message2)

message2 = f"\n{person.lower()} has {3*5} coins left"
print(message2)

message2 = f"\n{player['person']} has {player['coins']} coins left"
print(message2)

##you can pass formatting options
num = 15
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n") #:.2f formats it to 2 decimals

for num in range(1, 11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}\n") #:.2f formats it to 2 decimals

for num in range(1, 11):
    print(f"\n2.25 times {num} is {num / 2.27:.2%}") #:.2f formats it to 2 decimals