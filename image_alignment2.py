from PIL import Image

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

def find_offset(target, full_image):
    min_difference = float('inf')
    dx, dy = -1, -1
    for i in range(-15, 15):
        for j in range(-15, 15):
            score = 0
            # define target to be center of image
            target_size = 100
            x = (width - target_size) // 2
            y = (third - target_size) // 2
            for k in range(x, x + target_size):
                for l in range(y, y + target_size):
                    # find difference between target and full image
                    score += (target[k][l] - full_image[i + k][j + l]) ** 2
                    if score > min_difference:
                        break
            if score < min_difference:
                min_difference = score
                dx, dy = j, i
    return dx, dy

for i in range(1, 7):
    im = Image.open(f"images/im{i}.jpg")
    print("size", im.size)

    width, height = im.size[0], im.size[1]
    third = height // 3

    blue = im.crop((0, 0, im.size[0], third + 20))
    green = im.crop((0, third - 10, im.size[0], third * 2 + 10))
    red = im.crop((0, third * 2 - 10, im.size[0], third * 3))

    target_intensity = pixel_intensity(green)
    blue_intensity = pixel_intensity(blue)
    red_intensity = pixel_intensity(red)

    dx_g, dy_g = find_offset(target_intensity, blue_intensity)
    dx_r, dy_r = find_offset(target_intensity, red_intensity)

    print(f"blue offset: ({dx_g}, {dy_g})")
    print(f"red offset: ({dx_r}, {dy_r})")

    blue_aligned = blue.crop((dx_g, dy_g, dx_g + green.width, dy_g + green.height))
    red_aligned = red.crop((dx_r, dy_r, dx_r + green.width, dy_r + green.height))

    merged = Image.merge("RGB", (red_aligned, green, blue_aligned))
    merged.show()