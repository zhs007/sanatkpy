# -*- coding:utf-8 -*-
import random
from sanatkpy.atkresult import AtkResult
from sanatkpy.general import General

# 威震华夏 -
# 主动，35%，准备1回合
# 对敌军全体猛攻，伤害146%，并有50%概率使其进入缴械、技穷状态，独立判定，持续1回合
# 提升自己的伤害36%，持续2回合
# 如果自己为主将，控制概率提升至65%


def zfWZHX(atkRet: AtkResult, myindex: int, zfindex: int, curturn: int):
    # atkRet.clear()

    myinfo = atkRet.our[myindex]

    # for curturn in range(1, turnNums+1):
    if not myinfo.isReady(zfindex):
        if random.random() < 0.35:
            myinfo.setReady(zfindex, True)
    else:
        myinfo.setReady(zfindex, False)

        for i in range(1, 3 + 1):
            atkRet.addAttack(myindex, i, 1.46)
            if random.random() < 0.5:
                atkRet.addStatusJX(myindex, i, 1)
            if random.random() < 0.5:
                atkRet.addStatusJQ(myindex, i, 1)

        atkRet.addInDef(myindex, myindex, zfindex, 0.36, 2)
