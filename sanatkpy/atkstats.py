# -*- coding:utf-8 -*-
"""
    atkstats - 战斗统计
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long
from sanatkpy.utils import isSameArmy


class AtkStats:
    """
    AtkStats - 战斗统计
    """

    def __init__(self, myindex: int, zfindex: int, isChild: bool = False):
        """
        __init__ - 构造函数
        """

        # 这个为-1，表示是[0, 2]队伍的统计，如果为-2，表示是[3, 5]队伍的统计
        self.myindex = myindex

        self.zfindex = zfindex  # 这个为-1，表示是这个武将的总统计

        # 动态数据
        if not isChild:
            self.hlstats = AtkStats(myindex, zfindex, True)
        else:
            self.hlstats = None

        self._clear()

    def _clear(self):
        """
        _clear - clear
        """

        self.atkOutTotal = 0  # 造成的兵刃总伤害
        self.atkOut = [0, 0, 0, 0, 0, 0]  # 造成的兵刃伤害
        self.atkIn = [0, 0, 0, 0, 0, 0]  # 得到的兵刃伤害
        self.magicOutTotal = 0  # 造成的谋略总伤害
        self.magicOut = [0, 0, 0, 0, 0, 0]  # 造成的谋略伤害
        self.magicIn = [0, 0, 0, 0, 0, 0]  # 得到的谋略伤害

        # 技穷
        self.jqIn = 0
        self.jqOut = 0
        # 缴械
        self.jxIn = 0
        self.jxOut = 0

        if self.hlstats is not None:
            self.hlstats.clear()

    def clear(self):
        """
        clear - clear
        """

        self._clear()

    def _addAttack(self, src, zfindex: int, dest, atkper: float):
        """
        _addAttack - 增加兵刃伤害，这里不考虑混乱，混乱放addAttack处理
        """

        srcindex = src.index
        destindex = dest.index
        realzfindex = zfindex

        # if src.isHL():
        #     hlsrc, si1, zfi1 = src.getHLInfo()
        #     hlsrc.zf[zfi1].stats.hjlstats.
        # srcindex = si1
        # realzfindex = zfi1

        # 如果是武将数据统计
        if self.myindex >= 0:
            # 如果是武将技能统计，则不需要统计受击
            if self.zfindex >= 0:
                if self.zfindex == realzfindex and self.myindex == srcindex:
                    self.atkOutTotal += atkper
                    self.atkOut[destindex] += atkper
            else:  # 否则就是武将总统计，这里需要考虑输出和输入
                if srcindex == self.myindex:
                    self.atkOutTotal += atkper
                    self.atkOut[destindex] += atkper

                if destindex == self.myindex:
                    self.atkIn[srcindex] += atkper
        elif self.myindex == -1:  # 如果是队伍统计
            if src.index < 3:
                self.atkOutTotal += atkper
                self.atkOut[destindex] += atkper
            else:
                self.atkIn[srcindex] += atkper
        elif self.myindex == -2:  # 如果是队伍统计
            if src.index >= 3:
                self.atkOutTotal += atkper
                self.atkOut[destindex] += atkper
            else:
                self.atkIn[srcindex] += atkper

    def addAttack(self, src, zfindex: int, dest, atkper: float):
        """
        addAttack - 增加兵刃伤害
        """

        # srcindex = src.index
        # destindex = dest.index
        # realzfindex = zfindex

        if src.isHL():
            # 混乱时，如果对敌方的伤害，需要算到自己这边，如果是自己这边的伤害，要算到给你释放混乱的人上
            # 如果是自己人被混乱了，给你的混乱，应该计算到最初始的人，
            # 如果那次混乱已经结束，也需要记录下混乱根源
            # 其实这里可以不考虑给你混乱的人，只考虑根就好

            hlroot, rootzfi, _, _ = src.getHLInfo()

            # 如果混乱root和攻击目标是一边的，则这次攻击算发动者，也就是src
            # 否则算root的
            if isSameArmy(hlroot.index, dest.index):
                self._addAttack(src, zfindex, dest, atkper)
            else:
                hlroot.zf[rootzfi].stats.hjlstats._addAttack(src, zfindex, dest, atkper)
        else:
            self._addAttack(src, zfindex, dest, atkper)
