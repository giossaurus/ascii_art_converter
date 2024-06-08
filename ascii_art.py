from PIL import Image

# ASCII usado para definir intensidade e mais definição na imagem
ASCII_CHARS = "@%#*+=-:. "


def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    return image.convert("L")


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def main():
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = Image.open(path)
    except FileNotFoundError:
        print(f"{path} is not a valid pathname to an image.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    base_width = 100
    resized_image = resize_image(image, base_width)

    # Converte imagem para ASCII
    new_image_data = pixels_to_ascii(grayify(resized_image))

    # Formata a arte ASCII
    new_width, new_height = resized_image.size
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])

    # Printa o resultado
    print(ascii_image)

    # Salva o resultado em "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


# Roda o programa
if __name__ == "__main__":
    main()
