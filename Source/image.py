from PIL import Image

class Format:
    DDS = "DDS"
    PNG = "PNG"

class ImageConverter:

    def __init__(self) -> None:
        self.__images = []
    
    def Input(self, imagePath : list, enableAlpha = True):
        """ Store images with or without transparency. """

        for image in imagePath:
            # Store images with alpha channel
            if (enableAlpha):
                self.__images.append([image, Image.open(image).convert("RGBA")])

            # Store images without alpha channel
            else:
                self.__images.append([image, Image.open(image)])

    def ToDDS(self):
        """ Convert all of the input images to DDS files. """
        
        if (len(self.__images) > 0):
            counter = 0

            # Save the images with a different extention
            for image in self.__images:
                image[1].save(f"{image[0].split(".")[0]}.{Format.DDS.lower()}", format=Format.DDS)
                counter += 1
