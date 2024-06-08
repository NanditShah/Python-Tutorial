x = 10 # comment this line and you will get `NameError`
try:
    print(x)
    print(x/10) #change 10 to 0 and you will get `ZeroDivisionError` error
except NameError:
    print('Some variable is not defined')
except ZeroDivisionError:
    print('You can not divide variable with 0')
except:
    print('There is some error in code')
else:
    print('No error in code')
finally:
    print('This will get run no matter error is there or not')

try:
    raise NameError('NameError')
except Exception as error:
    print(error)

try:
    raise Exception('Mannually generated custom error, you can raise default python supported errors as well')
except Exception as error:
    print(error)

