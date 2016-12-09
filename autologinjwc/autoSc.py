# coding: utf-8

from selenium import webdriver
import Image
import os


def getCode():
    browser = webdriver.Firefox()
    url = "http://xk.autoisp.shu.edu.cn/"
    browser.get(url)
    browser.save_screenshot("codingpy.png")
    element = browser.find_element_by_css_selector('#Img1')
    left = int(element.location['x'])
    top = int(element.location['y'])
    right = int(element.location['x'] + element.size['width'])
    bottom = int(element.location['y'] + element.size['height'])

    im = Image.open("codingpy.png")
    im = im.crop((left, top, right, bottom))
    os.remove("codingpy.png")

    browser.close()
    browser.quit()

    return im
