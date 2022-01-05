# -*- coding:utf-8 -*-
"""
    atkresult - 战斗结果
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long

import random
from sanatkpy.general import General
from sanatkpy.atkstats import AtkStats
# from sanatkpy.buff import DefBuff


class AtkResult:
    """
        AtkResult - 战斗结果
    """

    def __init__(self):
        """
            构造函数
        """

        # self._clear()

        self.general = []

        for i in range(6):
            self.general.append(General(i))

        self.teamStats = [AtkStats(-1, -1), AtkStats(-2, -1)]

    # def _clear(self):
    #     """
    #         _clear - 清理基本属性
    #     """

    #     self.mnatk = 0              # 谋略伤害，百分比
    #     self.atk = 0                # 兵刃伤害，百分比
    #     self.zl = 0                 # 治疗，百分比
    #     self.fireLastTurns = 0      # 灼烧状态剩余回合
    #     self.waterLastTurns = 0     # 水攻状态剩余回合
    #     self.noBAtkLastTurns = 0    # 缴械状态剩余回合，无法进行普通攻击
    #     self.weakLastTurns = 0      # 虚弱状态剩余回合，无法造成伤害
    #     self.noZDLastTurns = 0      # 技穷状态剩余回合，无法发动主动技能

    def clear(self):
        """
            clear - 清理属性
        """

        # self._clear()

        for _, v in enumerate(self.general):
            v.clear()
            # self.our[i].clear()

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

        # if destindex > 0:
        #     # 正常，或者被混乱打到敌人
        #     destinfo = self.enemy[destindex - 1]

        #     self.atk += atk

        #     myinfo.atkOutTotal += atk
        #     myinfo.atkOut[destindex - 1] += atk

        #     destinfo.atkIn[myindex] += atk
        # else:
        #     # 被混乱，且打到自己人
        #     # 这里的输出要记到把你打成混乱的人身上
        #     destinfo = self.our[-destindex - 1]
        #     srcinfo = self.enemy[myinfo.HLSrc]

        #     destinfo.atkIn[myinfo.HLSrc] += atk
        #     srcinfo.HLAtk[myindex] += atk

    def addDefPer(self, myindex: int, zfindex: int, destindex: int, defper: float, turns: int):
        """
            addDefPer - 加/减 统率
        """

        myinfo = self.general[myindex]
        destinfo = self.general[destindex]

        destinfo.addDefPer(myinfo, zfindex, defper, turns)

    def addAtkOutPer(self, myindex: int, zfindex: int, destindex: int, atkoutper: float, turns: int):
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

        # myinfo.startAttack(zfindex, destinfo, atkper)

        # self.teamStats[0].addAttack(myinfo, zfindex, destinfo, atkper)
        # self.teamStats[1].addAttack(myinfo, zfindex, destinfo, atkper)

    # def addStatusJX(self, _myindex: int, destindex: int, turns: int):
    #     """
    #         addStatusJX - 增加缴械状态
    #     """

    #     # myinfo = self.our[myindex]

    #     if destindex > 0:
    #         # 正常，或者被混乱打到敌人
    #         destinfo = self.enemy[destindex - 1]

    #         if destinfo.noBAtkLastTurns == 0:
    #             destinfo.noBAtkLastTurns = turns
    #             self.noBAtkLastTurns += turns
    #     else:
    #         # 被混乱，且打到自己人
    #         # 这里的输出要记到把你打成混乱的人身上
    #         destinfo = self.our[-destindex - 1]

    #         if destinfo.noBAtkLastTurns == 0:
    #             destinfo.noBAtkLastTurns = turns
    #             # self.noBAtkLastTurns += turns

    # # destindex - [-3, 3]
    # def addStatusJQ(self, _myindex: int, destindex: int, turns: int):
    #     """
    #         addStatusJQ - 增加计穷状态
    #     """
    #     # myinfo = self.our[myindex]

    #     if destindex > 0:
    #         # 正常，或者被混乱打到敌人
    #         destinfo = self.enemy[destindex - 1]

    #         if destinfo.noZDLastTurns == 0:
    #             destinfo.noZDLastTurns = turns
    #             self.noZDLastTurns += turns
    #     else:
    #         # 被混乱，且打到自己人
    #         # 这里的输出要记到把你打成混乱的人身上
    #         destinfo = self.our[-destindex - 1]

    #         if destinfo.noZDLastTurns == 0:
    #             destinfo.noZDLastTurns = turns
    #             # self.noZDLastTurns += turns

    # # destindex - [-3, 3]
    # def addEnemyDownDef(self, myindex: int, destindex: int, zfindex: int, defper: float, turns: int):
    #     """
    #         addEnemyDownDef - 增加减防状态
    #     """

    #     myinfo = self.our[myindex]

    #     if destindex > 0:
    #         # 正常，或者被混乱打到敌人
    #         destinfo = self.enemy[destindex - 1]

    #         destinfo.addDefBuff(myindex, zfindex, defper, turns, False)
    #     else:
    #         # 被混乱，且打到自己人
    #         # 这里的输出要记到把你打成混乱的人身上
    #         destinfo = self.our[-destindex - 1]

    #         destinfo.addDefBuff(myinfo.HLSrc, zfindex, defper, turns, True)

    # # destindex - [-3, 3]
    # def addInDef(self, myindex: int, destindex: int, zfindex: int, defper: float, turns: int):
    #     """
    #         addInDef - 增加加防状态
    #     """

    #     myinfo = self.our[myindex]

    #     if destindex > 0:
    #         # 被混乱，加到敌人
    #         destinfo = self.enemy[destindex - 1]

    #         destinfo.addDefBuff(myindex, zfindex, defper, turns, False)
    #     else:
    #         # 正常，或混乱后，还是加到自己人
    #         destinfo = self.our[-destindex - 1]

    #         destinfo.addDefBuff(myinfo.HLSrc, zfindex, defper, turns, True)
