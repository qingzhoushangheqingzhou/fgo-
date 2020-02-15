#御主技能函数包
import os
import time as t
from util.battle_skill import tap,choosingservant,choosingenemy
#点击御主技能函数
def tappingskill_master(number):
    tap(1800,500)#御主技能
    t.sleep(1.5)
    if number == 1:
        tap(1370,500)#御主一技能
        t.sleep(3)
    if number == 2:
        tap(1500,500)#御主二技能
        t.sleep(3)
    if number == 3:
        tap(1630,500)#御主三技能
        t.sleep(3)
#华美的新年
def xinnian(number,target_servant = 1):
    if number == 1:#全体宝威
        tappingskill_master(number)
    else:#单体充能和加血
        tappingskill_master(number)
        choosingservant(target_servant)
#泳装，一技能己方全体，二三技能己方单体，和华美的新年完全一样
yongzhuang = xinnian
#极地服，三个技能都是己方单体
def jidi(number,target_servant = 1):
    tappingskill_master(number)
    choosingservant(target_servant)