# -*- coding:utf-8 -*-
"""
    zfbase - 战法基类
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long

import random
from sanatkpy.atkstats import AtkStats
from sanatkpy.atkresult import AtkResult
from sanatkpy.const import ConstValue


class ZFBase:
    """
    ZFBase - 战法基类
    """

    def __init__(self, index: int, zfindex: int, zftype: str, randStart: float):
        """
        构造函数
        """

        # 静态属性
        self.randStart = randStart
        self.isReadyMode = False
        self.readyTurns = 0
        self.name = "战法基类"
        self.typeLevel = "X"  # S/A/B
        self.index = index
        self.zfindex = zfindex
        self.zftype = zftype

        # 动态属性
        self.isReady = False
        self.curReadyTurns = 0
        self.stats = AtkStats(index, zfindex)

    def clear(self):
        """
        clear - 清除状态，清理动态属性
        """

        self.isReady = False
        self.curReadyTurns = 0

    def setBaseInfo(self, name: str, typeLevel: str):
        """
        setBaseInfo - 设置基本信息，静态属性
        """

        self.name = name
        self.typeLevel = typeLevel

    # def setRandStart(self, randStart):
    #     """
    #     setRandStart - 设置触发概率，静态属性
    #     """

    #     self.randStart = randStart

    def setReadyMode(self, isReadyMode: bool, readyTurns: int):
        """
        setReadyMode - 设置是否是需要准备的战法，静态属性
        """

        self.isReadyMode = isReadyMode
        self.readyTurns = readyTurns

    def setReady(self, isReady):
        """
        setReady - 设置准备状态，动态属性
        """

        self.isReady = isReady

        if isReady:
            self.curReadyTurns = self.readyTurns
        else:
            self.curReadyTurns = 0

    def onSimReady(self):
        """
            onSimReady - 准备状态

        Returns:
                -1  - 表示非准备战法
                0   - 表示未触发
                1   - 表示当前回合触发
                2   - 表示可以释放
                3   - 表示已触发，但还在准备状态中
        """

        if self.isReadyMode:
            if not self.isReady:
                if random.random() < self.randStart:
                    self.setReady(True)

                    return 1

                return 0
            else:
                if self.readyTurns == 0:
                    return 2

                return 3

        return -1

    def onReady(self, _atkRet: AtkResult):
        """
        onReady - 准备回合
        """

        return

    def onStart(self, _atkRet: AtkResult, _curturn: int):
        """
        onStart - 释放战法
        """

        return

    def procZDSkill(self, atkRet: AtkResult, curturn: int):
        """
        onZDSkill - 主动战法
        """

        ret = self.onSimReady()
        if ret == -1:
            if random.random() < self.randStart:
                self.onStart(atkRet, curturn)
        elif ret == 2:
            self.onStart(atkRet, curturn)

        return

    def onTurn(self, atkRet: AtkResult, curturn: int):
        """
        onTurn - 处理回合，0表示准备回合，1-8表示具体回合
        """

        if curturn == 0:
            if self.zftype == ConstValue.ZHZF or self.zftype == ConstValue.BDZF:
                self.onReady(atkRet)

            return

        if self.zftype == ConstValue.ZDZF:
            self.procZDSkill(atkRet, curturn)
