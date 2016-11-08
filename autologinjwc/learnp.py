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
    sumN = img.size[0] * img.size[1]
    sumP = 0
    for x in xrange(img.size[0]):
        for y in xrange(img.size[1]):
            sumP += img.getpixel((x, y))
    ttt = sumP / sumN
    ttt -= 29
    img = img.point(lambda x: 1 if x > ttt else 0, '1')
    clearNoise(img, 3, 5)
    return img


def colSplit(img):
    rowP = img.size[0] * [1]
    for i in xrange(1, img.size[1] - 1):
        for j in xrange(img.size[0]):
            rowP[j] = rowP[j] & img.getpixel((j, i))
    splitF = []
    rowP = [1, 1] + rowP + [1, 1, 1]
    l = 0
    r = 0
    for i in xrange(img.size[0]):
        if rowP[i + 2] == 1:
            if l < r:
                splitF += [l, r]
            l = i + 1
            r = l
        else:
            r = i + 1

    return splitF


def rowSplit(img):
    colP = img.size[1] * [1]
    for i in xrange(1, img.size[0] - 1):
        for j in xrange(img.size[1]):
            colP[j] = colP[j] & img.getpixel((i, j))
    splitF = []
    for i in xrange(img.size[1]):
        if colP[i + 2] == 0:
                splitF.append(i)
                break
    for i in xrange(0,img.size[1],-1):
        if colP[i + 2] == 0:
                splitF.append(i+1)
                break
    return splitF


def splitPic(num):
    im = Image.open('codeset/cleareddata/' + str(num) + '.png')
    splitF = colSplit(im)
    lens = len(splitF) / 2
    cnt = 0
    for i in range(lens):
        if (splitF[2 * i + 1] - splitF[2 * i]) <= 1 or (splitF[2 * i + 1] - splitF[2 * i]) > 16:
            continue
        splitIm = im.crop((splitF[2 * i], 0, splitF[2 * i + 1], 21))
        splitIm.save('codeset/splitdata/' + str(num) + '_' + str(cnt) + '.png')
        cnt += 1
    # for i in range(cnt):
    #     im = Image.open('codeset/splitdata/' +
    #                     str(num) + '_' + str(i) + '.png')
    #     splitF = rowSplit(im)
    #     splitIm = im.crop((0, splitF[0], im.size[0] - 1, splitF[-1]))
    #     splitIm.save('codeset/splitdata/' + str(num) + '_' + str(i) + '.png')

for i in range(20):
    splitPic(i)
