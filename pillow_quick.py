# library
import PIL
from PIL import Image

# read image using open() methid
img = Image.open("brad_pitt.jpg")
# display image using show() method.
img.show()

# print attributes
print(f"filename: {img.filename}")
print(f"size: {img.size}")
print(f"width: {img.width}")
print(f"height: {img.height}")
print(f"format: {img.format}")
print(f"mode: {img.mode}")

# resize image
(w,h) = (img.width//2, img.height//2)
res_img = img.resize((w,h))
# display the image
res_img.show()

# rotate image
# by 60' clockwise
theta = 60
# Angle is in degrees counter clockwise
rot_img = img.rotate(angle=theta)
# display the image
rot_img.show()

# crop image
# args: left, upper, right, left
crop_img = img.crop((50, 60, 140, 240))
# display image
crop_img.show()

# flip image
flip = img.transpose(PIL.Image.FLIP_TOP_BOTTOM)
# display
flip.show()

# save image
img.show()