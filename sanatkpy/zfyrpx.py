# -*- coding:utf-8 -*-
import random
from sanatkpy.atkresult import AtkResult
from sanatkpy.general import General
from sanatkpy.zfbase import ZFBase

# 燕人咆哮 -
# 被动，100%
# 第2、4回合，对敌军全体造成兵刃伤害104%，若对方处于缴械状态，降低统率50%，2回合
# 如果自己为主将，对技穷状态目标也降低统率


class YRPX(ZFBase):
    def __init__(self):
        super().__init__()

        self.setBaseInfo('燕人咆哮', 'S')
        self.setRandStart(1.0)
        # self.setReadyMode(True, 1)

    def onSim(self, atkRet: AtkResult, myindex: int, zfindex: int, curturn: int):
        myinfo = atkRet.our[myindex]

        if curturn == 2 or curturn == 4:
            for i in range(3):
                atkRet.addAttack(myindex, i + 1, 1.04)
                if atkRet.enemy[i].isNoBAtk():
                    atkRet.addEnemyDownDef(myindex, i + 1, zfindex, -0.5, 2)
                elif myindex == 0 and atkRet.enemy[i].isNoZD():
                    atkRet.addEnemyDownDef(myindex, i + 1, zfindex, -0.5, 2)

# def zfYRPX(atkRet: AtkResult, myindex: int, zfindex: int, curturn: int):
#     # atkRet.clear()

#     myinfo = atkRet.our[myindex]

#     # for curturn in range(1, turnNums+1):
#     if curturn == 2 or curturn == 4:
#         for i in range(3):
#             atkRet.addAttack(myindex, i + 1, 1.04)
#             if atkRet.enemy[i].isNoBAtk():
#                 atkRet.addEnemyDownDef(myindex, i + 1, zfindex, -0.5, 2)
#             elif myindex == 0 and atkRet.enemy[i].isNoZD():
#                 atkRet.addEnemyDownDef(myindex, i + 1, zfindex, -0.5, 2)
