# coding: utf-8

from PIL import Image, ImageDraw


def getPixel(image, x, y, N):
    L = image.getpixel((x, y))
    if L == 1:
        return 1
    nearDots = 0
    if L == image.getpixel((x - 1, y - 1)):
        nearDots += 1
    if L == image.getpixel((x - 1, y)):
        nearDots += 1
    if L == image.getpixel((x - 1, y + 1)):
        nearDots += 1
    if L == image.getpixel((x, y - 1)):
        nearDots += 1
    if L == image.getpixel((x, y + 1)):
        nearDots += 1
    if L == image.getpixel((x + 1, y - 1)):
        nearDots += 1
    if L == image.getpixel((x + 1, y)):
        nearDots += 1
    if L == image.getpixel((x + 1, y + 1)):
        nearDots += 1

    if nearDots < N:
        return 1
    else:
        return 0


def clearNoise(image, N, Z):
    draw = ImageDraw.Draw(image)

    for i in xrange(0, Z):
        for x in xrange(1, image.size[0] - 1):
            for y in xrange(1, image.size[1] - 1):
                color = getPixel(image, x, y, N)
                draw.point((x, y), color)


def clearPic(picNum):
    file_dir = 'codeset/'
    stype = 'rawdata/'
    dtype = 'cleareddata/'
    num = str(picNum)
    filePost = '.png'
    img = Image.open(file_dir + stype + num + filePost)
    img = img.convert("L")
    WHITE, BLACK = 255, 0
    sumN = img.size[0]*img.size[1]
    sumP =0
    for x in xrange(img.size[0]):
            for y in xrange(img.size[1]):
                sumP += img.getpixel((x, y))
    ttt = sumP/sumN
    ttt-=29
    img = img.point(lambda x: 1 if x > ttt else 0, '1')
    clearNoise(img, 3, 5)
    img.save(file_dir + dtype + num + filePost)


def main():
    for i in range(500):
        clearPic(i)
        print i


main()
