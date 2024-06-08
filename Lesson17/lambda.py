squared = lambda num : num * num

print(squared(10))
print(squared(12))

addTwo = lambda num : num + 2
print(addTwo(2))

addNum = lambda num1,num2 : num1 + num2
print(addNum(2,3))



# Higher order functions are the functions that either accepts function as an argument or return a function
# Clouser we have implement in prev lessos are also high-order function in a way
####################################

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
print(addTen(12))
print(addTen(14))
print(addTen(15))


addTwenty = funcBuilder(20)
print(addTen(12))
print(addTen(14))
print(addTen(15))


####################################

nums = [3,7,12,18,20,21]
squaredNums = list(map(lambda x : x**2,nums))
print(squaredNums)

evenNums = list(filter(lambda x : x % 2 == 0,nums))
print(evenNums)


from functools import reduce
total = reduce(lambda acc,curr : acc + curr,nums,0)
print(total)

names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']
charLen = reduce(lambda acc,curr : acc + len(curr),names,0)
print(charLen)
