# all caps means treat this as a constant,
# but it's not enforced :(
MEOWS = 3

for _ in range(MEOWS):
    print("meow")

print("--------")

# class variables help create constants too
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()
