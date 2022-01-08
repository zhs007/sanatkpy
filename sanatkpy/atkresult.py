# -*- coding:utf-8 -*-
"""
    atkresult - 战斗结果
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long

import random
from sanatkpy.general import General
from sanatkpy.atkstats import AtkStats
from sanatkpy.atkreport import AtkReport
from sanatkpy.utils import toPersentString


class AtkResult:
    """
    AtkResult - 战斗结果
    """

    def __init__(self, lstgeneral0: list, lstgeneral1: list):
        """
        构造函数
        """

        self.general = []

        self.general.extend(lstgeneral0)
        self.general.extend(lstgeneral1)
        # for i in range(6):
        #     self.general.append(None)

        self.teamStats = [AtkStats(-1, -1), AtkStats(-2, -1)]
        self.report = AtkReport()

    def clear(self):
        """
        clear - 清理属性
        """

        for _, v in enumerate(self.general):
            v.clear()

        for _, v in enumerate(self.teamStats):
            v.clear()

    def genEmenyIndex(self, myindex: int, nums: int, isHL: bool):
        """
        genEmenyIndex - 随机得到n个攻击目标，[0, 5]
        """

        arr = []
        if isHL:
            for i in range(6):
                if i != myindex:
                    arr.append(i)
        else:
            arr = []
            if myindex < 3:
                for i in range(3):
                    arr.append(3 + i)
            else:
                for i in range(3):
                    arr.append(i)

        destarr = []
        for i in range(nums):
            ri = int(random.random() * len(arr))
            destarr.append(arr[ri])
            del arr[ri]

        return destarr

    def isEnemy(self, myindex, destindex):
        """
        isEnemy - 随机得到1个攻击目标，[0, 5]
        """

        if myindex < 3:
            return destindex >= 3

        return destindex < 3

    def addAttack(self, myindex: int, zfindex: int, destindex: int, atkper: float):
        """
        addAttack - 增加兵刃伤害
        """

        myinfo = self.general[myindex]
        destinfo = self.general[destindex]

        myinfo.startAttack(zfindex, destinfo, atkper)

        self.teamStats[0].addAttack(myinfo, zfindex, destinfo, atkper)
        self.teamStats[1].addAttack(myinfo, zfindex, destinfo, atkper)

        self.report.addLineEx(
            "#general# 对 #enemy# 造成 #atkper# 的兵刃伤害",
            {
                "general": myinfo.name,
                "enemy": destinfo.name,
                "atkper": toPersentString(atkper),
            },
        )

    def addDefPer(
        self, myindex: int, zfindex: int, destindex: int, defper: float, turns: int
    ):
        """
        addDefPer - 加/减 统率
        """

        myinfo = self.general[myindex]
        destinfo = self.general[destindex]

        destinfo.addDefPer(myinfo, zfindex, defper, turns)

    def addAtkOutPer(
        self, myindex: int, zfindex: int, destindex: int, atkoutper: float, turns: int
    ):
        """
        addAtkOutPer - 加/减 兵刃伤害百分比
        """

        myinfo = self.general[myindex]
        destinfo = self.general[destindex]

        destinfo.addAtkOutPer(myinfo, zfindex, atkoutper, turns)

    def addJX(self, myindex: int, zfindex: int, destindex: int, turns: int):
        """
        addJX - 缴械
        """

        myinfo = self.general[myindex]
        destinfo = self.general[destindex]

        destinfo.addJX(myinfo, zfindex, turns)

    def addJQ(self, myindex: int, zfindex: int, destindex: int, turns: int):
        """
        addJQ - 技穷
        """

        myinfo = self.general[myindex]
        destinfo = self.general[destindex]

        destinfo.addJQ(myinfo, zfindex, turns)

    def onTurn(self, curturn: int):
        """
        onTurn - 处理回合，0表示准备回合，1-8表示具体回合
        """

        if curturn == 0:
            self.report.addPart("准备回合")
        else:
            self.report.addPart(f"回合{curturn}")

        for _, v in enumerate(self.general):
            v.onTurn(self, curturn)
