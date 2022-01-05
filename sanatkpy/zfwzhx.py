# -*- coding:utf-8 -*-
"""
    zfwzhx - 威震华夏

    主动，35%，准备1回合
    对敌军全体猛攻，伤害146%，并有50%概率使其进入缴械、技穷状态，独立判定，持续1回合
    提升自己的伤害36%，持续2回合
    如果自己为主将，控制概率提升至65%
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long

import random
from sanatkpy.atkresult import AtkResult
# from sanatkpy.general import General
from sanatkpy.zfbase import ZFBase
from sanatkpy.utils import isMainGeneral


class WZHX(ZFBase):
    """
        WZHX - 威震华夏
    """

    def __init__(self, index: int, zfindex: int):
        """
            构造函数
        """
        super().__init__(index, zfindex)

        self.setBaseInfo('威震华夏', 'S')
        self.setRandStart(0.35)
        self.setReadyMode(True, 1)

    def onTurn(self, atkRet: AtkResult, _curturn: int):
        """
            onTurn - 处理回合，0表示准备回合，1-8表示具体回合
        """

        myindex = self.index
        zfindex = self.zfindex

        per = 0.5
        if isMainGeneral(self.index):
            per = 0.65

        retReady = self.onSimReady()
        if retReady == 2:
            for i in range(1, 3 + 1):
                atkRet.addAttack(myindex, i, 1.46)

                if random.random() < per:
                    atkRet.addJX(myindex, i, 1)
                if random.random() < per:
                    atkRet.addJQ(myindex, i, 1)

            atkRet.addAtkOutPer(myindex, myindex, zfindex, 0.36, 2)

    # def onSim(self, atkRet: AtkResult, myindex: int, zfindex: int, _curturn: int):
    #     """
    #         onSim - 释放战法
    #     """
    #     # myinfo = atkRet.our[myindex]

    #     retReady = self.onSimReady()
    #     if retReady == 2:
    #         for i in range(1, 3 + 1):
    #             atkRet.addAttack(myindex, i, 1.46)

    #             if random.random() < 0.5:
    #                 atkRet.addStatusJX(myindex, i, 1)
    #             if random.random() < 0.5:
    #                 atkRet.addStatusJQ(myindex, i, 1)

    #         atkRet.addInDef(myindex, myindex, zfindex, 0.36, 2)
