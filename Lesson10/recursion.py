def add_one(limit,initialValue):
    if(initialValue >= limit):
        return initialValue
    
    return add_one(limit,initialValue+1);

calculatedValue = add_one(10,-1)
print(calculatedValue)