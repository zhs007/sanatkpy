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
from sanatkpy.const import ConstValue


class WZHX(ZFBase):
    """
    WZHX - 威震华夏
    """

    def __init__(self, src, zfindex: int):
        """
        构造函数
        """
        super().__init__(
            src, zfindex, "威震华夏", ConstValue.ZFLEVEL_S, ConstValue.ZDZF, 0.35
        )

        # self.setBaseInfo("威震华夏", ConstValue.ZFLEVEL_S)
        # self.setRandStart(0.35)
        self.setReadyMode(True, 1)

    def onStart(self, atkRet: AtkResult, _curturn: int):
        """
        onStart - 释放战法
        """

        myindex = self.src.index
        zfindex = self.zfindex
        myinfo = self.src

        per = 0.5
        if isMainGeneral(self.src.index):
            per = 0.65

        arr = atkRet.genEmenyIndex(myindex, 3, myinfo.isHL())

        for _, vi in enumerate(arr):
            atkRet.addAttack(myindex, zfindex, vi, 1.46)

            if random.random() < per:
                atkRet.addJX(myindex, zfindex, vi, 1)
            if random.random() < per:
                atkRet.addJQ(myindex, zfindex, vi, 1)

        atkRet.addAtkOutPer(myindex, zfindex, myindex, 0.36, 2)
