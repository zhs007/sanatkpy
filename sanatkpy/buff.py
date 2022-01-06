# -*- coding:utf-8 -*-
"""
    buff - Buff
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long
# from sanatkpy.utils import isSameArmy


class BaseBuff:
    """
    BaseBuff - Buff基类
    """

    def __init__(self, code: str, name: str, src, zfindex: int, dest, lastturns: int):
        """
        构造函数
        """

        # 静态属性
        self.code = code
        self.name = name

        # 动态属性
        self.src = src
        self.zfindex = zfindex
        self.dest = dest
        self.lastTurns = lastturns

        self.hlroot = None
        self.hlrootzfindex = -1

        if src.isHL():
            r0, rzfi0, _, _ = src.getHLInfo()

            self.hlroot = r0
            self.hlrootzfindex = rzfi0

        # if isSameArmy(src.index, dest.index):

    def onTurns(self):
        """
        onTurns - 每个回合开始调用
        """
        if self.lastTurns > 0:
            self.lastTurns -= 1

    def isSame(self, buff):
        """
        isSame - 是否是同类Buff
        """
        return self.code == buff.code

    def merge(self, buff) -> bool:
        """
        merge - 2个同类状态需要处理，返回True表示已经处理完了，返回False表示无法merge，只能添加
        """
        if self.code == buff.code:
            return self.onMerge(buff)

        return False

    def onMerge(self, _buff) -> bool:
        """
        onMerge - 具体的合成方式，返回True表示已经处理完了，返回False表示无法merge，只能添加
        """
        return False

    def canBaseAttack(self, _src):
        """
        canBaseAttack - 是否可以普通攻击
        """

        return True

    def canImmunity(self, _dest):
        """
        canImmunity - 是否可以免疫这种buff
        """

        return False

    def canZDSkill(self, _src):
        """
        canZDSkill - 是否可以释放主动战法
        """

        return True

    def inSnapshot(self, _statusSnapshot) -> bool:
        """
        isInSnapshot - 是否应该保留进快照里
        """

        return False

    def onTurn(self, _atkRet, _curturn: int):
        """
        onTurn - 处理回合，0表示准备回合，1-8表示具体回合
        """

        return
