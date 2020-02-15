#截图，裁切并保存助战图片
import os
from PIL import Image
os.chdir("F:\\fgo\\assets\\tem")#更改python工作目录
os.system('adb shell screencap -p /sdcard/sh.png')
os.system('adb pull /sdcard/sh.png .')
img1 = Image.open("sh.png")
im = img1.transpose(Image.ROTATE_90)   # 逆时针旋转，270可以引用其他想要旋转的角度（固定的常量值，如90,180,270等）
im.save("sh.png")
im = Image.open("sh.png")
# 图片的宽度和高度
img_size = im.size
print("图片宽度和高度分别是{}".format(img_size))
'''
裁剪：传入一个元组作为参数
元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
'''
# 截取图片中一块宽和高都是250的
x = 480
y = 210
w = 120
h = 130
region = im.crop((x, y, x+w, y+h))
region.save("./yuzhezhisuo.png")