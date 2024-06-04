mytuple = tuple(('Dave', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

# which values will be considerd in *variable depends on it's position while destructuring
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))