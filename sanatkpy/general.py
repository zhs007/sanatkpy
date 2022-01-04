# -*- coding:utf-8 -*-
"""
    general - 武将
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long

from sanatkpy.buff import DefBuff
from sanatkpy.status import Status
from sanatkpy.atkstats import AtkStats


class General:
    """
        General - 武将
    """

    def __init__(self, index: int):
        """
            构造函数
        """

        # 静态属性
        self.index = index
        self.zf = [None, None, None]    # 战法

        # 动态属性
        self.status = Status()
        self.stats = AtkStats(index, -1)

        self._clear()

    def _clear(self):
        """
            _clear - 清理数据
        """

        self.atkOutTotal = 0            # 造成的兵刃总伤害
        self.atkOut = [0, 0, 0]         # 造成的兵刃伤害
        self.atkIn = [0, 0, 0]          # 得到的兵刃伤害

        self.defOutTotal = 0            # 造成的总减防
        self.defOut = [0, 0, 0]         # 造成的减防
        self.defInTotal = 0             # 得到的总减防
        self.defIn = [0, 0, 0]          # 得到的减防
        self.defArr = []                # 统率buff队列

        self.mnatkPer = 0               # 谋略伤害百分比，正增加负降低
        self.atkPer = 0                 # 兵刃伤害百分比，正增加负降低
        self.defPer = 0                 # 统率百分比，正增加负降低

        # 自己被混乱了
        self.HLSrc = 0                  # 混乱来源，自己被谁混乱了
        self.HLLastTurns = 0            # 混乱剩余回合数，自己混乱的剩余回合数

        # 自己混乱了别人
        self.HLAtk = [0, 0, 0]          # 自己混乱敌人并造成的总伤害，这个伤害是兵刃伤害率，所以要分人统计
        self.HLNoBAtkTimes = 0          # 自己混乱敌人并造成敌人缴械状态回合次，混乱的人造成敌人缴械次数
        self.HLDefOutTotal = 0          # 自己混乱敌人，并造成敌人减防

        self.NoBAtkTimes = 0            # 造成敌人缴械状态回合次

        self.fireLastTurns = 0          # 灼烧状态剩余回合
        self.fireAtkPer = 0             # 灼烧伤害率
        self.waterLastTurns = 0         # 水攻状态剩余回合
        self.waterAtkPer = 0            # 水攻伤害率
        self.jjLastTurns = 0            # 急救状态剩余回合
        self.jjPer = 0                  # 急救回复率
        self.noBAtkLastTurns = 0        # 缴械状态剩余回合，无法进行普通攻击
        self.weakLastTurns = 0          # 虚弱状态剩余回合，无法造成伤害
        self.noZDLastTurns = 0          # 技穷状态剩余回合，无法发动主动技能

        for i, _v in enumerate(self.zf):
            self.zf[i].clear()

        self.status.clear()

        # self.zf = [None, None, None]    # 战法
        # self.ready = [                  # 战法准备状态
        #     False,
        #     False,
        #     False
        # ]

    def clear(self):
        """
            clear - 清理数据
        """

        self._clear()

    def addZF(self, zfindex: int, zf):
        """
            addZF - 增加战法
        """

        self.zf[zfindex] = zf

    # def isReady(self, zfindex):
    #     return self.ready[zfindex]

    # def setReady(self, zfindex, ready):
    #     self.ready[zfindex] = ready

    def addDefBuff(self, srcindex: int, zfindex: int, defper: float, lastturns: int, isHL: bool):
        """
            addDefBuff - 增加防御Buff
        """

        buf = DefBuff(srcindex, zfindex, defper, lastturns, isHL)

        self.defArr.append(buf)

        self.defInTotal += buf.defPer

        if not isHL:
            self.defIn[srcindex] += buf.defPer

    def addHL(self, srcindex: int, turns: int):
        """
            addHL - 增加混乱Buff
        """

        if self.HLLastTurns == 0:
            self.HLSrc = srcindex
            self.HLLastTurns = turns

    def isNoBAtk(self):
        """
            isNoBAtk - 是否可以普通攻击
        """

        return self.noBAtkLastTurns > 0

    def isNoZD(self):
        """
            isNoZD - 是否可以释放主动战法
        """

        return self.noZDLastTurns > 0

    def isHL(self):
        """
            isHL - 是否混乱中
        """

        return self.status.hasBuff('hl')

    def getHLIndex(self) -> tuple:
        """
            getHLIndex - 获取导致自己混乱的人
        """

        hlindex = self.status.findBuff('hl')
        if hlindex >= 0:
            return self.status.lstBuff[hlindex].srcIndex, self.status.lstBuff[hlindex].zfIndex

        return -1, -1
