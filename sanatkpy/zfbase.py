# -*- coding:utf-8 -*-
# pylint: disable = invalid-name
# pylint: disable = line-too-long

import random
from sanatkpy.atkresult import AtkResult
from sanatkpy.general import General

# 战法


class ZFBase:
    def __init__(self):
        # 静态属性
        self.randStart = 0
        self.isReadyMode = False
        self.readyTurns = 0
        self.name = '战法基类'
        self.typeLevel = 'X'    # S/A/B

        # 动态属性
        self.isReady = False
        self.curReadyTurns = 0

    def clear(self):
        self.isReady = False
        self.curReadyTurns = 0

    def setBaseInfo(self, name: str, typeLevel: str):
        self.name = name
        self.typeLevel = typeLevel

    def setRandStart(self, randStart):
        self.randStart = randStart

    def setReadyMode(self, isReadyMode: bool, readyTurns: int):
        self.isReadyMode = isReadyMode
        self.readyTurns = readyTurns

    def setReady(self, isReady):
        self.isReady = isReady

        if isReady:
            self.curReadyTurns = self.readyTurns
        else:
            self.curReadyTurns = 0

    # onSimReady
    #   -1  - 表示非准备战法
    #   0   - 表示未触发
    #   1   - 表示当前回合触发
    #   2   - 表示可以释放
    #   3   - 表示已触发，但还在准备状态中
    def onSimReady(self):
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

    # def onSim(self, atkRet: AtkResult, myindex: int, zfindex: int, curturn: int):
    #     myinfo = atkRet.our[myindex]

    #     # for curturn in range(1, turnNums+1):
    #     if not myinfo.isReady(zfindex):
    #         if random.random() < 0.35:
    #             myinfo.setReady(zfindex, True)
    #     else:
    #         myinfo.setReady(zfindex, False)

    #         for i in range(1, 3 + 1):
    #             atkRet.addAttack(myindex, i, 1.46)
    #             if random.random() < 0.5:
    #                 atkRet.addStatusJX(myindex, i, 1)
    #             if random.random() < 0.5:
    #                 atkRet.addStatusJQ(myindex, i, 1)

    #         atkRet.addInDef(myindex, myindex, zfindex, 0.36, 2)
