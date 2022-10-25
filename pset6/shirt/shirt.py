import sys
import os
from PIL import Image, ImageOps


def main():
    verify_args()
    verify_ext([".jpg", ".jpeg", ".png"])

    # open both images
    try:
        img1 = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"Input does not exist")

    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("shirt image does not exist")

    # resize and crop "before" image
    # according to size of shirt image
    img1 = ImageOps.fit(img1, shirt.size)

    # overlay shirt image, indicating it as mask
    img1.paste(shirt, shirt)

    # save composite
    img1.save(sys.argv[2])


def verify_args():
    # verify exactly 3 args passed
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


def verify_ext(valid_ext):
    # split filenames into file and ext
    file1, ext1 = os.path.splitext(sys.argv[1])
    file2, ext2 = os.path.splitext(sys.argv[2])

    # verify filenames have identical, valid ext
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")
    if ext1 not in valid_ext:
        sys.exit("Invalid file extensions")


if __name__ == "__main__":
    main()
