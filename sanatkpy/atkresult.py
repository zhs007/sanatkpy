# -*- coding:utf-8 -*-
"""
    atkresult - 战斗结果
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long

import random
from sanatkpy.general import General
# from sanatkpy.buff import DefBuff


class AtkResult:
    """
        AtkResult - 战斗结果
    """

    def __init__(self):
        """
            构造函数
        """

        self._clear()

        self.enemy = [General(), General(), General()]
        self.our = [General(), General(), General()]

    def _clear(self):
        """
            _clear - 清理基本属性
        """

        self.mnatk = 0              # 谋略伤害，百分比
        self.atk = 0                # 兵刃伤害，百分比
        self.zl = 0                 # 治疗，百分比
        self.fireLastTurns = 0      # 灼烧状态剩余回合
        self.waterLastTurns = 0     # 水攻状态剩余回合
        self.noBAtkLastTurns = 0    # 缴械状态剩余回合，无法进行普通攻击
        self.weakLastTurns = 0      # 虚弱状态剩余回合，无法造成伤害
        self.noZDLastTurns = 0      # 技穷状态剩余回合，无法发动主动技能

    def clear(self):
        """
            clear - 清理属性
        """

        self._clear()

        for i in range(3):
            self.enemy[i].clear()
            self.our[i].clear()

    def genEmenyIndex(self, myindex: int, isHL: bool):
        """
            genEmenyIndex - 随机得到敌人
        """

        if isHL:
            arr = [1, 2, 3]
            for i in range(3):
                if i != myindex:
                    arr.append(-(i + 1))

            ri = int(random.random() * 5)
            return arr[ri]
        else:
            ri = int(random.random() * 3)

            return ri + 1

    # destindex - [-3, 3]
    def addAttack(self, myindex: int, destindex: int, atk: float):
        """
            addAttack - 增加兵刃伤害
        """

        myinfo = self.our[myindex]

        if destindex > 0:
            # 正常，或者被混乱打到敌人
            destinfo = self.enemy[destindex - 1]

            self.atk += atk

            myinfo.atkOutTotal += atk
            myinfo.atkOut[destindex - 1] += atk

            destinfo.atkIn[myindex] += atk
        else:
            # 被混乱，且打到自己人
            # 这里的输出要记到把你打成混乱的人身上
            destinfo = self.our[-destindex - 1]
            srcinfo = self.enemy[myinfo.HLSrc]

            destinfo.atkIn[myinfo.HLSrc] += atk
            srcinfo.HLAtk[myindex] += atk

    # destindex - [-3, 3]
    def addStatusJX(self, _myindex: int, destindex: int, turns: int):
        """
            addStatusJX - 增加缴械状态
        """

        # myinfo = self.our[myindex]

        if destindex > 0:
            # 正常，或者被混乱打到敌人
            destinfo = self.enemy[destindex - 1]

            if destinfo.noBAtkLastTurns == 0:
                destinfo.noBAtkLastTurns = turns
                self.noBAtkLastTurns += turns
        else:
            # 被混乱，且打到自己人
            # 这里的输出要记到把你打成混乱的人身上
            destinfo = self.our[-destindex - 1]

            if destinfo.noBAtkLastTurns == 0:
                destinfo.noBAtkLastTurns = turns
                # self.noBAtkLastTurns += turns

    # destindex - [-3, 3]
    def addStatusJQ(self, _myindex: int, destindex: int, turns: int):
        """
            addStatusJQ - 增加计穷状态
        """
        # myinfo = self.our[myindex]

        if destindex > 0:
            # 正常，或者被混乱打到敌人
            destinfo = self.enemy[destindex - 1]

            if destinfo.noZDLastTurns == 0:
                destinfo.noZDLastTurns = turns
                self.noZDLastTurns += turns
        else:
            # 被混乱，且打到自己人
            # 这里的输出要记到把你打成混乱的人身上
            destinfo = self.our[-destindex - 1]

            if destinfo.noZDLastTurns == 0:
                destinfo.noZDLastTurns = turns
                # self.noZDLastTurns += turns

    # destindex - [-3, 3]
    def addEnemyDownDef(self, myindex: int, destindex: int, zfindex: int, defper: float, turns: int):
        """
            addEnemyDownDef - 增加减防状态
        """

        myinfo = self.our[myindex]

        if destindex > 0:
            # 正常，或者被混乱打到敌人
            destinfo = self.enemy[destindex - 1]

            destinfo.addDefBuff(myindex, zfindex, defper, turns, False)
        else:
            # 被混乱，且打到自己人
            # 这里的输出要记到把你打成混乱的人身上
            destinfo = self.our[-destindex - 1]

            destinfo.addDefBuff(myinfo.HLSrc, zfindex, defper, turns, True)

    # destindex - [-3, 3]
    def addInDef(self, myindex: int, destindex: int, zfindex: int, defper: float, turns: int):
        """
            addInDef - 增加加防状态
        """

        myinfo = self.our[myindex]

        if destindex > 0:
            # 被混乱，加到敌人
            destinfo = self.enemy[destindex - 1]

            destinfo.addDefBuff(myindex, zfindex, defper, turns, False)
        else:
            # 正常，或混乱后，还是加到自己人
            destinfo = self.our[-destindex - 1]

            destinfo.addDefBuff(myinfo.HLSrc, zfindex, defper, turns, True)
