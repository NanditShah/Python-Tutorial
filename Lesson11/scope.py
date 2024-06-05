# global keyword to update any global scoped varibale in function or code block
# nonlocal keyword to update any parent function or parent code block varibale in child function or code block

name = "Dave"
count = 1


def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")

another()