# -*- coding:utf-8 -*-
"""
    atkstats - 战斗统计
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long


class AtkStats:
    """
        AtkStats - 战斗统计
    """

    def __init__(self, myindex: int, zfindex: int):
        """
            __init__ - 构造函数
        """

        # 这个为-1，表示是[0, 2]队伍的统计，如果为-2，表示是[3, 5]队伍的统计
        self.myindex = myindex

        self.zfindex = zfindex                  # 这个为-1，表示是这个武将的总统计

        self.atkOutTotal = 0                    # 造成的兵刃总伤害
        self.atkOut = [0, 0, 0, 0, 0, 0]        # 造成的兵刃伤害
        self.atkIn = [0, 0, 0, 0, 0, 0]         # 得到的兵刃伤害
        self.magicOutTotal = 0                  # 造成的谋略总伤害
        self.magicOut = [0, 0, 0, 0, 0, 0]      # 造成的谋略伤害
        self.magicIn = [0, 0, 0, 0, 0, 0]       # 得到的谋略伤害

    def addAttack(self, src, zfindex: int, dest, atkper: float):
        srcindex = src.index
        destindex = dest.index
        realzfindex = zfindex

        if src.isHL():
            si1, zfi1 = src.getHLIndex()
            srcindex = si1
            realzfindex = zfi1

        # 如果是武将数据统计
        if self.myindex >= 0:
            # 如果是武将技能统计，则不需要统计受击
            if self.zfindex >= 0:
                if self.zfindex == realzfindex and self.myindex == srcindex:
                    self.atkOutTotal += atkper
                    self.atkOut[destindex] += atkper
            else:   # 否则就是武将总统计，这里需要考虑输出和输入
                if srcindex == self.myindex:
                    self.atkOutTotal += atkper
                    self.atkOut[destindex] += atkper

                if destindex == self.myindex:
                    self.atkIn[srcindex] += atkper
        elif self.myindex == -1:    # 如果是队伍统计
            if src.index < 3:
                self.atkOutTotal += atkper
                self.atkOut[destindex] += atkper
            else:
                self.atkIn[srcindex] += atkper
        elif self.myindex == -2:    # 如果是队伍统计
            if src.index >= 3:
                self.atkOutTotal += atkper
                self.atkOut[destindex] += atkper
            else:
                self.atkIn[srcindex] += atkper