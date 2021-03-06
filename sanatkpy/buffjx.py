# -*- coding:utf-8 -*-
"""
    buffjx - BuffJX 缴械
"""
from sanatkpy.buff import BaseBuff

# pylint: disable = invalid-name
# pylint: disable = line-too-long


class BuffJX(BaseBuff):
    """
    BuffJX - 缴械
    """

    def __init__(self, src, zfindex, dest, lastturns: int):
        """
        构造函数
        """

        super().__init__("jx", "缴械", src, zfindex, dest, lastturns)

    def onMerge(self, _buff) -> bool:
        """
        onMerge - 抛弃掉新buff
        """
        return True

    def canBaseAttack(self, _src):
        """
        canBaseAttack - 缴械无法进行普通攻击，但需要先遍历buff，是否有免疫缴械的
        """

        # if src.status.canImmunity(self):
        #     return True

        return False
