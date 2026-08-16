def main():
    expression = input("Expression: ").strip()

    #Sets x, y, z for easy manipulation
    x_str, y, z_str = separator(expression)

    #Converts strings to floats
    x = float(x_str.strip())
    z = float(z_str.strip())

    match y:
        case "+":
            print(x + z)
        case "-":
            print(x - z)
        case "/":
            print(f"{x / z :.1f}")
        case "*":
            print(f"{x * z :.1f}")

def separator(sample):
    if "+" in sample:
        return sample.partition("+")
    elif "-" in sample:
        return sample.partition("-")
    elif "/" in sample:
        return sample.partition("/")
    elif "*" in sample:
        return sample.partition("*")

main()
