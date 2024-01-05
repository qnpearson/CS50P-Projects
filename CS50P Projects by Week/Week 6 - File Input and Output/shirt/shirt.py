from PIL import Image
import sys
import numpy
from PIL import ImageOps

def main():
    check()

def check():
    good_list = ["jpg","png"]
    if len(sys.argv) == 3:
        suffix1 = sys.argv[1].split(".")
        suffix2 = sys.argv[2].split(".")
        if suffix1[1] not in good_list:
            sys.exit("Invalid input")
        else:
            if suffix2[1] not in good_list:
                sys.exit("Invalid input")
            else:
                if suffix1[1] != suffix2[1]:
                    sys.exit("Input and output have different extensions")
                else:
                    animate()
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

def animate():
    shirt = Image.open("shirt.png")
    shirt_size = shirt.size
    try:
        with Image.open(sys.argv[1]) as before_image:
            new_before_image = ImageOps.fit(before_image, shirt_size)
            new_before_image.paste(im=shirt, mask=shirt)
            new_before_image.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()