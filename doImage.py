from PIL import Image

IMAGES_PATH = 'images/'

file_open = "alex.jpg"  # input("Name of file: ")
file_load = "file.txt"  # input("Name of text file: ")

image = Image.open(IMAGES_PATH + file_open)
width_image = image.size[0]
height_image = image.size[1]
pixels_class = image.load()  # unload pixels

variants = ["♦", "#", "$", "&", "N", "%", "M", "H", "P", "K", \
            "Z", "T", "?", "/", ":", "."]

# variants = "QWERTYUIOP[]';LKJHGFDSAZXCBNM,./"  # for the thrill
coefficient = len(variants)


def txt_file_by_image(pixels, size_x: int, size_y: int):
    global height_image, width_image

    returned: str = ""

    for y in range(size_y):
        for x in range(size_x):
            r, g, b = pixels[x, y]
            index = ((r + g + b)//3 * coefficient) // 255 - 1
            # print(index)
            returned += variants[index]
        returned += "\n"
    with open(file_load, "w", encoding="utf-8") as file_output:
        file_output.write(returned)  # Clean the document and print result


txt_file_by_image(pixels=pixels_class, size_x=width_image, size_y=height_image)

