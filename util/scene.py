#导入各种库
import os
import time as t
import cv2
from PIL import Image
#点击函数，接收要点击的坐标
def tap(x0,y0):
    adbtap = 'adb shell input tap {x1} {y1}'.format(x1=x0,y1=y0)   #利用str.format实现字符串的格式化
    os.system(adbtap)#即adb调用操作os.system('adb shell input tap x y')
#判断函数，接收要搜索的小图
def scenejudge(mould):
    os.system('adb shell screencap -p /sdcard/sh.png')
    os.system('adb pull /sdcard/sh.png .')
    img1 = Image.open("sh.png")
    im = img1.transpose(Image.ROTATE_90)   # 逆时针旋转，90可以引用其他想要旋转的角度（固定的常量值，如90,180，270等）
    im.save("sh.png")
    img = cv2.imread('sh.png', 0)
    template = cv2.imread(mould,0)
    res= cv2.matchTemplate(img,template, cv2.TM_CCOEFF_NORMED)#原图在左，要搜索的图在右
    thresholdSTART = 0.9
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res, None)
    if(max_val>=thresholdSTART):
        #print(max_val)
        #print(max_loc)
        return (0,max_loc,max_val)
    else:
        #print(max_val)
        #print(max_loc)
        return (1,max_loc,max_val)
#吃苹果函数，接收整数，1吃金，非1吃银
def apples(int):
    if (scenejudge('apple.png') [0]== 0):
        if (int==1):
            tap(980,480)
            t.sleep(3)
            tap(1210,880)
            t.sleep(3)
        else:
            tap(980,660)
            t.sleep(3)
            tap(1210,880)
            t.sleep(3)
#搜索助战函数，接收要搜索的助战，没有就刷新，有就点击助战
def support(mould):
    while scenejudge('support.png')[0]:#判断是否进入选助战界面
        t.sleep(0.2)
    while scenejudge(mould)[0]:#找助战
        tap(1300,200)                   #找不到就刷新
        t.sleep(1.5)
        tap(1210,830)                   #确认刷新
        t.sleep(2)
        if(scenejudge(mould)[0]==0):
            break
        t.sleep(10)
    tap(scenejudge(mould)[1][0]+120,scenejudge(mould)[1][1]+115)#选择助战
#结束函数，接收素材和关卡图,素材输入0时不检索素材
def finish(level,i,assets):
    while scenejudge('bond.png' or 'bond2.png')[0]:
        t.sleep(0.2)
    tap(200,760)
    while scenejudge('master.png')[0]:
        t.sleep(0.2)
    tap(200,760)
    while scenejudge('win.png')[0]:
        t.sleep(0.2)
    if(assets != 0):
        if(scenejudge(assets)[0] == 0):#刷到书页了i加1
            i = i + 1
    tap(1800,1000)
    t.sleep(3)
    while scenejudge(level)[0]:
        t.sleep(0.2)