from PIL import Image, ImageChops

im = Image.open("images/im2.jpg")
print("size", im.size)

# im.show()

third = im.size[1]/3

blue = im.crop((0, 0, im.size[0], third + 20))
green = im.crop((0, third, im.size[0], third * 2 + 20))
red = im.crop((0, third * 2, im.size[0], third * 3))

# blue.show()
# green.show()
# red.show()

target_size = 30
x = (400 - target_size) / 2
y = (340 - target_size) / 2
target_area = blue.crop((x, y, x + target_size, y + target_size))
# target_area.show()

def pixel_intensity(image):
    width, height = image.size
    image = image.convert("RGB")
    pixels = image.load()
    
    intensity = []
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = pixels[x, y]
            row.append((r + g + b) / 3)  # convert to grayscale
        intensity.append(row)
    
    return intensity

target_intensity = pixel_intensity(target_area)
green_intensity = pixel_intensity(green)
red_intensity = pixel_intensity(red)

def find_offset(target, full_image):
    target_h, target_w = len(target), len(target[0])
    image_h, image_w = len(full_image), len(full_image[0])
    min_difference = 100000000
    dx, dy = -1, -1
    for i in range(image_h - target_h):
        for j in range(image_w - target_w):
            total_difference = 0
            for x in range(target_h):
                for y in range(target_w):
                    total_difference += abs(target[x][y] - full_image[i + x][j + y])
                    if total_difference > min_difference:
                        break
            if total_difference < min_difference:
                min_difference = total_difference
                dx, dy = j, i
    return dx, dy

dx_g, dy_g = find_offset(target_intensity, green_intensity)
dx_g -= x
dy_g -= y
dx_r, dy_r = find_offset(target_intensity, red_intensity)
dx_r -= x
dy_r -= y

print(f"green offset: ({dx_g}, {dy_g})")
print(f"red offset: ({dx_r}, {dy_r})")