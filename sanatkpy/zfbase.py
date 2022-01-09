# -*- coding:utf-8 -*-
"""
    zfbase - 战法基类
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long

import random
from sanatkpy.atkstats import AtkStats
from sanatkpy.const import ConstValue


class ZFBase:
    """
    ZFBase - 战法基类
    """

    def __init__(
        self,
        src,
        zfindex: int,
        name: str,
        typeLevel: str,
        zftype: str,
        randStart: float,
    ):
        """
        构造函数
        """

        # 静态属性
        self.randStart = randStart
        self.isReadyMode = False
        self.readyTurns = 0
        self.name = name
        self.typeLevel = typeLevel  # S/A/B
        self.src = src
        self.zfindex = zfindex
        self.zftype = zftype
        self.src = src

        # 动态属性
        self.isReady = False
        self.curReadyTurns = 0
        self.stats = AtkStats(src.index, zfindex)

    def clear(self):
        """
        clear - 清除状态，清理动态属性
        """

        self.isReady = False
        self.curReadyTurns = 0

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
                -3  - 表示未发动非准备战法
                -2  - 表示非准备战法被Cancel
                -1  - 表示发动非准备战法
                0   - 表示未触发
                1   - 表示当前回合触发准备
                2   - 表示可以释放
                3   - 表示已触发，但还在准备状态中
                4   - 表示未准备状态下被Cancel
                5   - 表示准备状态下被Cancel
        """

        if self.isReadyMode:
            if not self.isReady:
                if not self.src.canZDSkill():
                    return 4

                if random.random() < self.randStart:
                    self.setReady(True)

                    return 1

                return 0
            else:
                if not self.src.canZDSkill():
                    self.setReady(False)

                    return 5

                if self.readyTurns == 0:
                    return 2

                return 3

        if random.random() < self.randStart:
            if self.src.canZDSkill():
                return -1

            return -2

        return -3

    def onReady(self, _atkRet):
        """
        onReady - 准备回合
        """

        return

    def onStart(self, _atkRet, _curturn: int):
        """
        onStart - 释放战法
        """

        return

    def procZDSkill(self, atkRet, curturn: int):
        """
        onZDSkill - 主动战法
        """

        ret = self.onSimReady()
        if ret == -1:
            atkRet.report.addParagraphEx(
                f"{self.src.name} 发动 {self.name}",
                "#general# 发动 #zf#",
                {
                    "general": self.src.name,
                    "zf": self.name,
                },
            )

            self.onStart(atkRet, curturn)
        elif ret == 2:
            atkRet.report.addParagraphEx(
                f"{self.src.name} {self.name} 准备完成，发动 {self.name}",
                "#general# #zf# 准备完成，发动 #zf#",
                {
                    "general": self.src.name,
                    "zf": self.name,
                },
            )

            self.onStart(atkRet, curturn)
        elif ret == 1:
            atkRet.report.addParagraphEx(
                f"{self.src.name} 准备发动 {self.name}",
                "#general# 准备发动 #zf#",
                {
                    "general": self.src.name,
                    "zf": self.name,
                },
            )
        elif ret == -2:
            atkRet.report.addParagraphEx(
                f"{self.src.name} 发动 {self.name} 被打断",
                "#general# 发动 #zf# ，被打断",
                {
                    "general": self.src.name,
                    "zf": self.name,
                },
            )
        elif ret == 4:
            atkRet.report.addParagraphEx(
                f"{self.src.name} 准备发动 {self.name} 被打断",
                "#general# 准备发动 #zf# ，被打断",
                {
                    "general": self.src.name,
                    "zf": self.name,
                },
            )
        elif ret == 5:
            atkRet.report.addParagraphEx(
                f"{self.src.name} 准备发动 {self.name} 中，被打断",
                "#general# 准备发动 #zf# 中，被打断",
                {
                    "general": self.src.name,
                    "zf": self.name,
                },
            )

        return

    def onTurn(self, atkRet, curturn: int):
        """
        onTurn - 处理回合，0表示准备回合，1-8表示具体回合
        """

        if curturn == 0:
            if self.zftype == ConstValue.ZHZF or self.zftype == ConstValue.BDZF:
                self.onReady(atkRet)

            return

        if self.zftype == ConstValue.ZDZF:
            self.procZDSkill(atkRet, curturn)
        elif self.zftype == ConstValue.BASEATK:
            if self.src.canBaseAttack():
                self.onStart(atkRet, curturn)

    def onStartTurn(self, _atkRet, curturn: int):
        """
        onStartTurn - 处理回合开始，0表示准备回合，1-8表示具体回合
        """

        if curturn > 0:
            if self.isReadyMode:
                if self.isReady:
                    self.readyTurns -= 1
