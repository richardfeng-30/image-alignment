from PIL import Image

im = Image.open("images/im2.jpg")
print("size", im.size)

# im.show()


print ("width", im.size[0])
#width number of colums

print ("height", im.size[1])
#height number of rows

third = im.size[1]/3

blue = im.crop((0, 15, im.size[0], third + 15))
green = im.crop((0, third + 1 + 10, im.size[0], third * 2 + 10))
red = im.crop((0, third * 2 + 5, im.size[0], third * 3 + 5))

blue.show()
green.show()
red.show()

print(blue.size)
print(green.size)
print(red.size)

merged = Image.merge("RGB", (red,green,blue))

merged.show()