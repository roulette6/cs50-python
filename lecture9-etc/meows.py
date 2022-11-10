# argparse imports sys to get args
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

# you don't have to cast to int b/c parser
# is handling that
for _ in range(args.n):
    print("meow")
