from image import ImageConverter

if __name__ == "__main__":
    application = ImageConverter()
    application.Input(["Data/tree.png"])
    application.ToDDS()
