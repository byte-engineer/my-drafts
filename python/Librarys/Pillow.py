# Draft/Librarys/PIL.py

#(Pillow)----------------------------------------------
#|> Python Imaging Library (PIL)
#|> We use this library to edit images.
#|> pip install Pillow.
#|> It's wepsite https://pillow.readthedocs.io
import os
os.system('cls')

from PIL import Image

# Open image
myimage = Image.open(r"C:\Users\Hp\Desktop\bilal\files\Codes\Python\Draft\REQs\fisherman.jpg")

# show image
myimage.show()

# image data
print(myimage.format, myimage.size, myimage.mode)

# crop an image
box = (100, 100, 1600, 1200)
croped = myimage.crop(box)
croped.show()

# Resize the image
new_resolution = (80, 60)                                               # Specify the new width and height
resized_image = myimage.resize(new_resolution)

BWimage = myimage.convert("L")

# save an image
resized_image.save("Draft/REQs/fisherman_resized.jpg")

# Access a single pixel
pixel = myimage.getpixel((100, 100))                                    # Coordinates of the pixel|Pixel = (129, 177, 199)

# Replace pixel
new_pixel = (255, 0, 0)
myimage.putpixel((100, 100), new_pixel)

