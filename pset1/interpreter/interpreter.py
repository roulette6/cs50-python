def main():
    x, y, z = input("Expression: ").strip().split(" ")

    answer = calculate(x, y, z)

    print(f"{answer:.1f}")


def calculate(x, operator, z):
    x = int(x)
    z = int(z)

    match operator:
        case "+":
            return float(x + z)
        case "-":
            return float(x - z)
        case "*":
            return float(x * z)
        case "/":
            return float(x / z)


main()