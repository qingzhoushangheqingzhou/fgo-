#导入各种库
import os
import time as t
import cv2
from PIL import Image
#更改工作目录
os.chdir("F:\\fgo\\assets\\tem")
from util.scene import *
from util.battle_skill import tappingskill_servant,choosingservant,choosingenemy,cba
from util.battle_cards import npsingle,arashisp
from util.cos import yongzhuang
for i in range(6):
    #选择关卡
    tap(1300,300)
    t.sleep(3)
    #如果没体力了吃银苹果
    apples(2)
    #选择助战
    support('CBA.png')
    #开始战斗
    while scenejudge('standby.png')[0]:
        t.sleep(0.2)
    tap(1800,1000)
    while scenejudge('attack.png')[0]:
        t.sleep(0.2)
    #第一面
    tappingskill_servant(1,2)
    tappingskill_servant(3,2)
    choosingenemy(2)
    arashisp()
    while scenejudge('attack.png')[0]:
        t.sleep(0.2)
    #第二面
    cba(2)
    tappingskill_servant(2,1)
    npsingle(2)
    #第三面
    while scenejudge('attack.png')[0]:
        t.sleep(0.2)
    cba(1,1)
    cba(3,1)
    yongzhuang(1)
    npsingle(1)
    finish('katejia.png',i,0)
    print(i)