# -*- coding:utf-8 -*-
"""
    zfwzhx - 燕人咆哮

    被动，100%
    第2、4回合，对敌军全体造成兵刃伤害104%，若对方处于缴械状态，降低统率50%，2回合
    如果自己为主将，对技穷状态目标也降低统率
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long

# import random
from sanatkpy.atkresult import AtkResult
from sanatkpy.zfbase import ZFBase
from sanatkpy.utils import isMainGeneral
from sanatkpy.buff import BaseBuff
from sanatkpy.const import ConstValue


class BuffYRPXReady(BaseBuff):
    """
    YRPX - 燕人咆哮
    """

    def __init__(self, src, zfindex: int, dest):
        """
        构造函数
        """

        super().__init__("yrpxready", "燕人咆哮 - 准备", src, zfindex, dest, -1)

    def onTurn(self, atkRet: AtkResult, curturn: int):
        """
        onTurn - 处理回合，0表示准备回合，1-8表示具体回合
        """

        myindex = self.src.index
        zfindex = self.zfindex
        myinfo = atkRet.general[myindex]

        if curturn == 2 or curturn == 4:
            arr = atkRet.genEmenyIndex(myindex, 3, myinfo.isHL())

            for _, vi in enumerate(arr):
                atkRet.addAttack(myindex, vi, 1.04)

                if atkRet.general[vi].canBaseAttack():
                    atkRet.addDefPer(myindex, zfindex, vi, -0.5, 2)
                elif isMainGeneral(myindex) and atkRet.general[vi].canZDSkill():
                    atkRet.addDefPer(myindex, zfindex, vi, -0.5, 2)


class YRPX(ZFBase):
    """
    YRPX - 燕人咆哮
    """

    def __init__(self, index: int, zfindex: int):
        """
        构造函数
        """
        super().__init__(index, zfindex, ConstValue.BDZF, 1)

        self.setBaseInfo("燕人咆哮", "S")
        # self.setRandStart(1.0)
        # self.setReadyMode(True, 1)

    def onReady(self, atkRet: AtkResult):
        """
        onReady - 准备回合
        """

        myindex = self.index
        zfindex = self.zfindex
        myinfo = atkRet.general[myindex]

        myinfo.addBuff(BuffYRPXReady(myinfo, zfindex, myinfo))
