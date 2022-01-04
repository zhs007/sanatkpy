# -*- coding:utf-8 -*-
"""
    buffjq - BuffJQ 技穷
"""
from sanatkpy.buff import BaseBuff
# pylint: disable = invalid-name
# pylint: disable = line-too-long


class BuffJQ(BaseBuff):
    """
        BuffJQ - 计穷
    """

    def __init__(self, srcindex: int, zfindex: int, destindex: int, lastturns: int, isHL: bool):
        """
            构造函数
        """

        super().__init__("jq", srcindex, zfindex, destindex, lastturns, isHL)

    def onMerge(self, _buff) -> bool:
        """
            onMerge - 抛弃掉新buff
        """
        return True

    def canZDSkill(self, src):
        """
            canZDSkill - 是否可以释放主动战法
        """

        if src.status.canImmunity(self):
            return True

        return True
