#从者技能函数包
import os
import time as t
#点击函数，接收要点击的坐标
def tap(x0,y0):
    adbtap = 'adb shell input tap {x1} {y1}'.format(x1=x0,y1=y0)   #利用str.format实现字符串的格式化
    os.system(adbtap)#即adb调用操作os.system('adb shell input tap x y')
#点击从者技能函数（手机屏幕1920*1080），接收从者位置（1,2,3）和技能序号（1,2,3）
def tappingskill_servant(number,position):
    if position == 1:
        if number == 1:
            tap(100,880)
        if number == 2:
            tap(240,880)
        if number == 3:
            tap(380,880)
        t.sleep(3)
    if position == 2:
        if number == 1:
            tap(570,880)
        if number == 2:
            tap(720,880)
        if number == 3:
            tap(870,880)
        t.sleep(3)
    if position == 3:
        if number == 1:
            tap(1060,880)
        if number == 2:
            tap(1210,880)
        if number == 3:
            tap(1360,880)
        t.sleep(3)
#选择己方目标函数,接收要选择的位置（1,2,3）
def choosingservant(target_servant):
    if target_servant == 1:
        tap(600,600)
    if target_servant == 2:
        tap(980,600)
    if target_servant == 3:
        tap(1450,600)
    t.sleep(3)
#选择敌方目标函数，接收要选择的位置（1,2,3）
def choosingenemy(target_enemy):
    if target_enemy == 1:
        tap(100,100)
    if target_enemy == 2:
        tap(500,100)
    if target_enemy == 3:
        tap(900,100)
    t.sleep(3)
#CBA
def cba(number,target_servant = 2,position = 3):
    if number == 2:#敌方全体降防
        tappingskill_servant(number,position)
    else:#单体绿魔放和充能
        tappingskill_servant(number,position)
        choosingservant(target_servant)
#孔明
def kongming(number,target_servant = 2,position = 3):
    if number == 3:#单体暴伤
        tappingskill_servant(number,position)
        choosingservant(target_servant)
    else:#全体加防加攻
        tappingskill_servant(number,position)