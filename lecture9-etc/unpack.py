# variable number of positional arguments
def f(*args, **kwargs):
    if args:
        print("Positional:", args)
    if kwargs:
        print("Named:", kwargs)


f(100, 50, 25, 5)
print()
f(galleons=100, sickles=50, knuts=25)


"""
def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

# * will unpack a list for
# positional arguments
print(total(*coins), "knuts")


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# ** will unpack a dict for
# named arguments
print(total(**coins))

"""
