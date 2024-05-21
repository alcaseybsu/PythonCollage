#Leah Casey
#Delaware County - 10/22/21

from PIL import Image, ImageEnhance, ImageOps

def collage():
    src = Image.open("barn.jpg")
    mod1 = src.copy()
    mod2 = src.copy()
    mod3 = src.copy()
    mod4 = src.copy()

    canvas_width = src.width * 3
    canvas_height = src.height * 2
    canvas = Image.new("RGB", (canvas_width, canvas_height))

    sig = Image.open("sig.jpg")
    sig = sig.resize((sig.width // 10, sig.height // 10))

    for i in range(15):
        slice_image(src, int(src.width * i / 15), int(src.width * (i + 1) / 15), canvas, int(src.width * (i * 2) / 15), 0)

    slice_image(src, 0, int(src.width * 1 / 15), canvas, 0, 0)  # slice, upper left

    mod1 = mirror_right_to_left(mod1)
    mod2 = lighten(mod2)
    mod3 = mirror_vertical(mod3)

    copy(mod1, canvas, src.width * 2, src.height)
    copy(mod2, canvas, src.width * 2, 0)
    copy(mod3, canvas, 0, src.height)  # original
    copy(mod4, canvas, src.width, src.height)

    #chroma_sig(sig, canvas, 750, 525)

    canvas.show()
    canvas.save("leah_casey.jpg")

def copy(pic, target, targX, targY):
    target.paste(pic, (targX, targY))

def mirror_right_to_left(img):
    return ImageOps.mirror(img)

def lighten(img):
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(1.5)

def slice_image(src, slice_start, slice_end, target, targX, targY):
    for x in range(slice_start, slice_end):
        for y in range(src.height):
            pixel = src.getpixel((x, y))
            target.putpixel((targX + x - slice_start, targY + y), pixel)

def mirror_vertical(img):
    return ImageOps.flip(img)

#def chroma_sig(src, target, targetX, targetY):
#    src = src.convert("RGBA")
#    datas = src.getdata()

    #new_data = []
    #for item in datas:
        # Change all white (also shades of whites)
        # pixels to transparent
        #if item[0] in list(range(200, 256)):
        #    new_data.append((255, 255, 255, 0))
        #else:
        #    new_data.append(item)

    #src.putdata(new_data)
    #target.paste(src, (targetX, targetY), src)

collage()
