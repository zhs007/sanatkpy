# -*- coding:utf-8 -*-
"""
    baseatk - 普通攻击

    就是100%的兵刃攻击
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long
from sanatkpy.zfbase import ZFBase
from sanatkpy.const import ConstValue


class BaseAtk(ZFBase):
    """
    BaseAtk - 普通攻击
    """

    def __init__(self, src, zfindex: int):
        """
        构造函数
        """
        super().__init__(
            src, zfindex, "普通攻击", ConstValue.ZFLEVEL_N, ConstValue.BASEATK, 1
        )

        # self.setBaseInfo("普通攻击", ConstValue.ZFLEVEL_N)
        # self.setRandStart(0.35)
        # self.setReadyMode(True, 1)

    def onStart(self, atkRet, _curturn: int):
        """
        onStart - 释放战法
        """

        atkRet.report.addParagraphEx(
            f"{self.src.name} 发动普通攻击",
            "#general# 发动 #zf#",
            {
                "general": self.name,
                "zf": self.name,
            },
        )

        myindex = self.src.index
        zfindex = self.zfindex
        myinfo = self.src

        arr = atkRet.genEmenyIndex(myindex, 1, myinfo.isHL())

        for _, vi in enumerate(arr):
            atkRet.addAttack(myindex, zfindex, vi, 1)
