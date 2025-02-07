from PIL import Image

im = Image.open("images/im1.jpg")
print("size", im.size)

# im.show()

width, height = im.size[0], im.size[1]
third = height // 3

blue = im.crop((0, 0, im.size[0], third + 20))
green = im.crop((0, third - 10, im.size[0], third * 2 + 10))
red = im.crop((0, third * 2 - 10, im.size[0], third * 3))

blue.show()
green.show()
red.show()

target_size = 20
x = (width - target_size) // 2
y = (third - target_size) // 2
print(x, y)
target_area = blue.crop((x, y, x + target_size, y + target_size))
target_area.show()

# transform into single intensity array
def pixel_intensity(image):
    width, height = image.size
    image = image.convert("RGB")
    pixels = image.load()
    
    intensity = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(pixels[x, y][0]) #RGB are the same
        intensity.append(row)
    
    return intensity

target_intensity = pixel_intensity(target_area)
green_intensity = pixel_intensity(green)
red_intensity = pixel_intensity(red)

def find_offset(target, full_image):
    target_h, target_w = len(target), len(target[0])
    image_h, image_w = len(full_image), len(full_image[0])
    min_difference = float('inf')
    dx, dy = -1, -1
    # loop through full image
    for i in range(image_h - target_h):
        for j in range(image_w - target_w):
            total_difference = 0
            for x in range(target_h):
                for y in range(target_w):
                    # find difference between target and full image
                    total_difference += abs(target[x][y] - full_image[i + x][j + y])
                    if total_difference > min_difference:
                        break
            if total_difference < min_difference:
                min_difference = total_difference
                dx, dy = j, i
    print(dx, dy)
    return dx, dy

dx_g, dy_g = find_offset(target_intensity, green_intensity)
dx_g -= x
dy_g -= y
dx_r, dy_r = find_offset(target_intensity, red_intensity)
dx_r -= x
dy_r -= y

print(f"green offset: ({dx_g}, {dy_g})")
print(f"red offset: ({dx_r}, {dy_r})")

# use dimensions of blue image
green_aligned = green.crop((dx_g, dy_g, dx_g + blue.width, dy_g + blue.height))
red_aligned = red.crop((dx_r, dy_r, dx_r + blue.width, dy_r + blue.height))

merged = Image.merge("RGB", (blue, green_aligned, red_aligned))
merged.show()