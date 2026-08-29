import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    format = [".jpg", ".jpeg", ".png"]
    f_index = sys.argv[1].rfind(".")
    s_index = sys.argv[2].rfind(".")

    if sys.argv[1][f_index:].lower() not in format:
        sys.exit("Invalid input")
    elif sys.argv[2][s_index:].lower() not in format:
        sys.exit("Invalid output")
    elif sys.argv[1][f_index:].lower() != sys.argv[2][s_index:].lower():
        sys.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        muppit = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    size = shirt.size
    muppit = ImageOps.fit(muppit, size)
    muppit.paste(shirt, shirt)
    muppit.save(sys.argv[2])

if __name__ == "__main__":
    main()
