from PIL import Image

im = Image.open("images/duck.jpg")

#display
# im.show()

#size is a tuple - multiple value like array
print("size", im.size)

print ("width", im.size[0])
#width number of colums

print ("height", im.size[1])
#height number of rows

#loads image as 2d pixel array
pixels = im.load()

print (pixels[0,0])


#colum and then row
print (pixels[899,1199])

r, g, b = pixels[0,0]
print("red at 0, 0: ", r)

print ("blue at 0, 0: ", pixels[0,0][2])


mid = im.size[1]/2

for x in range (im.size[0]):
    pixels[x, mid] = (0,0,0)


#crop to keep top half


#left, top, right, bottom
cropped = im.crop((0,0,im.size[0],mid))

cropped.show()

cropped2 = im.crop((0,0,im.size[0],mid+100))

cropped2.show()

cropped.save("croppedduck.jpg")


blueduck = Image.new("RGB", (im.size[0], im.size[1]))

blueduck.px = blueduck.load()

for x in range (0, im.size[0]):
    for y in range (0, im.size[1]):
        r,g,b = pixels[x,y]
        if r > 140 and g > 140 and b > 140:
            r = 0
            g = 0
            b = 255
        blueduck.px[x,y] = (r,g,b)

blueduck.show()

#treat as black and white
red,green,blue = im.split()



red.show()
green.show()
blue.show()
red_px = red.load()
print("red at 0,0", red_px[0,0])

merged = Image.merge("RGB", (red,green,blue))
merged.show()


