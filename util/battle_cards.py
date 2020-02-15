#选卡函数包
import os
import time as t
#点击函数，接收要点击的坐标
def tap(x0,y0):
    adbtap = 'adb shell input tap {x1} {y1}'.format(x1=x0,y1=y0)   #利用str.format实现字符串的格式化
    os.system(adbtap)#即adb调用操作os.system('adb shell input tap x y')
#大英雄，充完能就爆
def arashi():
    tap(380,880)#大英雄充能
    t.sleep(3)
    tap(1800,1000)#攻击
    t.sleep(5)
    tap(620,300)#一号位宝具卡
    t.sleep(1.5)
    tap(200,760)#第一张指令卡
    t.sleep(1.5)
    tap(575,760)#第二张指令卡
#先选普通指令卡再选大英雄宝具
def arashisp():
    tap(1800,1000)#攻击
    t.sleep(5)
    tap(200,760)#第一张指令卡
    t.sleep(1.5)
    tap(575,760)#第二张指令卡
    t.sleep(1.5)
    tap(620,300)#一号位宝具卡
#单人宝具函数（一张宝具卡和第一、二张普通卡），接收宝具卡位置1和2
def npsingle(k):
    tap(1800,1000)#攻击
    t.sleep(5)
    if(k == 1):
        tap(620,300)#一号宝具卡
    if(k == 2):
        tap(960,300)#二号宝具卡
    t.sleep(1.5)
    tap(200,760)
    t.sleep(1.5)
    tap(575,760)