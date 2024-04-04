import os, sys
from PIL import Image

class Format:
    DDS = "DDS"
    PNG = "PNG"

class ImageConverter:

    def __init__(self) -> None:
        self.__images = []
        self.__inputPath = ""
        self.__outputPath = ""
    
    def Input(self, imagePath : list, enableAlpha = True):
        """ Store images with or without transparency. It can be a relative path or an absolute one. """

        # Calls the presentation header
        self.__ShowHeader()

        files = []
        self.__inputPath = imagePath
        self.__outputPath = f"{self.__inputPath}\\_Output"

        # Gives feedback to the user
        print("\nReading files . . .")
        counter = 0

        # Read all files inside the given folder
        for entry in os.listdir(self.__inputPath):
            path = os.path.join(self.__inputPath, entry)

            # Check if the entry is a file
            if os.path.isfile(path):
                files.append(path)

        # Store images with or without alpha channel
        for image in files:
            if (enableAlpha):
                self.__images.append([image, Image.open(image).convert("RGBA")])

            else:
                self.__images.append([image, Image.open(image)])

            # Calls and update the progress bar
            counter += 1
            self.__ProgressBar(counter, len(files))

    def ToDDS(self):
        """ Convert all of the input images to DDS files. """
        if (len(self.__images) > 0):

            # Gives feedback to the user
            print("\n\nConverting to DDS format . . .")
            counter = 0

            # Creates the output folder
            self.__CreateFolder(self.__outputPath)

            # Save the images with a different extention
            for image in self.__images:
                IMAGE = str(image[0]).split("\\")
                image[1].save(f"{self.__outputPath}\\{IMAGE[-1].split(".")[0]}.{Format.DDS.lower()}", format=Format.DDS)

                # Calls and update the progress bar
                counter += 1
                self.__ProgressBar(counter, len(self.__images))

            # Gives feedback to the user
            print("\n\n================ [Conversion Completed] ================\n")

    def __CreateFolder(self, folderPath):
        """ Creates a folder if it doesn't exist. """
        if (not os.path.exists(folderPath)):
            os.makedirs(folderPath)

    def __ProgressBar(self, iteration, total, barLength=50):
        """ Creates and updates a progress bar. """
        percent = f"{100 * (iteration / float(total)):.2f}"
        filledLength = int(barLength * iteration // total)
        bar = '■' * filledLength + '-' * (barLength - filledLength)
        sys.stdout.write(f'\r[{bar}] {percent}%')
        sys.stdout.flush()

    def __ShowHeader(self):
        """ Shows the header. """
        HEADER = "| Image Converter | Version 1.2.0 | By Kellvyn Sampaio |"

        print("=" * len(HEADER))
        print(HEADER)
        print("=" * len(HEADER))
