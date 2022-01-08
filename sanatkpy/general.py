# -*- coding:utf-8 -*-
"""
    general - 武将
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long
from sanatkpy.buffhl import BuffHL
from sanatkpy.buffjx import BuffJX
from sanatkpy.buffjq import BuffJQ
from sanatkpy.buffdef import BuffDef
from sanatkpy.buffdefper import BuffDefPer
from sanatkpy.buffatkoutper import BuffAtkOutPer
from sanatkpy.status import Status
from sanatkpy.atkstats import AtkStats
from sanatkpy.baseatk import BaseAtk


class General:
    """
    General - 武将
    """

    def __init__(self, index: int, name: str):
        """
        构造函数
        """

        # 静态属性
        self.index = index
        self.zf = [None, None, None, BaseAtk(index, 3)]  # 战法
        self.name = name

        # 动态属性
        self.status = Status()
        self.stats = AtkStats(index, -1)

    def clear(self):
        """
        clear - 清理数据
        """

        for i, _v in enumerate(self.zf):
            self.zf[i].clear()

        self.status.clear()

    def addZF(self, zfindex: int, zf):
        """
        addZF - 增加战法
        """

        self.zf[zfindex] = zf

    def addDef(self, src, zfindex: int, defval: int, lastturns: int):
        """
        addDef - 增加防御Buff
        """

        buf = BuffDef(src, zfindex, self, lastturns, defval)
        self.status.addBuff(buf)

    def addDefPer(self, src, zfindex: int, defper: float, lastturns: int):
        """
        addDefPer - 增加防御Buff
        """

        buf = BuffDefPer(src, zfindex, self, lastturns, defper)
        self.status.addBuff(buf)

    def addAtkOutPer(self, src, zfindex: int, atkoutper: float, lastturns: int):
        """
        addAtkOutPer - 兵刃伤害百分比Buff
        """

        buf = BuffAtkOutPer(src, zfindex, self, lastturns, atkoutper)
        self.status.addBuff(buf)

    def addHL(self, src, zfindex: int, turns: int):
        """
        addHL - 增加混乱Buff
            注意，混乱也可以被混乱的自己人添加
        """

        buf = BuffHL(src, zfindex, self, turns)
        self.status.addBuff(buf)

    def addJX(self, src, zfindex: int, turns: int):
        """
        addJX - 增加缴械Buff
        """

        buf = BuffJX(src, zfindex, self, turns)
        self.status.addBuff(buf)

    def addJQ(self, src, zfindex: int, turns: int):
        """
        addJQ - 增加技穷Buff
        """

        buf = BuffJQ(src, zfindex, self, turns)
        self.status.addBuff(buf)

    def addBuff(self, buf):
        """
        addBuff - 增加Buff
        """

        self.status.addBuff(buf)

    def canBaseAttack(self):
        """
        canBaseAttack - 是否可以普通攻击
        """

        return self.status.canBaseAttack(self)

    def canZDSkill(self):
        """
        canZDSkill - 是否可以释放主动战法
        """

        return self.status.canZDSkill(self)

    def isHL(self):
        """
        isHL - 是否混乱中
        """

        return self.status.hasBuff("hl")

    def getHLInfo(self) -> tuple:
        """
        getHLInfo - 获取导致自己混乱的人

        Returns:
            (root, rootzfindex, src, zfindex)
        """

        hlindex = self.status.findBuff("hl")
        if hlindex >= 0:
            return (
                self.status.lstBuff[hlindex].hlroot,
                self.status.lstBuff[hlindex].hlrootzfindex,
                self.status.lstBuff[hlindex].src,
                self.status.lstBuff[hlindex].zfindex,
            )

        return None, -1, None, -1

    def startAttack(self, zfindex: int, dest, atkper: float):
        """
        startAttack - 兵刃攻击
        """

        self.stats.addAttack(self, zfindex, dest, atkper)
        self.zf[zfindex].stats.addAttack(self, zfindex, dest, atkper)

    def onTurn(self, atkRet, curturn: int):
        """
        onTurn - 处理回合，0表示准备回合，1-8表示具体回合
        """

        # myindex = self.index
        # myinfo = atkRet.general[myindex]

        if curturn == 0:
            atkRet.report.addParagraphEx(
                f"{self.name} 开始准备",
                "#general# 开始准备",
                {
                    "general": self.name,
                },
            )

            for i, v in enumerate(self.zf):
                if i == 3:  # 准备阶段，跳过普通攻击
                    return

                if v is not None:
                    v.onTurn(atkRet, curturn)

            return

        atkRet.report.addParagraphEx(
            f"{self.name} 开始行动",
            "#general# 开始行动",
            {
                "general": self.name,
            },
        )

        self.status.onTurn(atkRet, curturn)

        for i, v in enumerate(self.zf):
            if v is not None:
                v.onTurn(atkRet, curturn)
