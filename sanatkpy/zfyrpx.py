# -*- coding:utf-8 -*-
import random
from sanatkpy.atkresult import AtkResult
from sanatkpy.general import General

# 燕人咆哮 -
# 被动，100%
# 第2、4回合，对敌军全体造成兵刃伤害104%，若对方处于缴械状态，降低统率50%，2回合
# 如果自己为主将，对技穷状态目标也降低统率


def zfYRPX(atkRet: AtkResult, myindex: int, zfindex: int, turnNums: int):
    atkRet.clear()

    myinfo = atkRet.our[myindex]

    for curturn in range(1, turnNums+1):
        if curturn == 2 or curturn == 4:
            atkRet.addAttack(myindex, 0, 1.04)
            atkRet.addAttack(myindex, 1, 1.04)
            atkRet.addAttack(myindex, 2, 1.04)
