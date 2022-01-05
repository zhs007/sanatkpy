# -*- coding:utf-8 -*-
"""
    buffatkoutper - BuffAtkOutPer 兵刃伤害buff百分比
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long
from sanatkpy.buff import BaseBuff


class BuffAtkOutPer(BaseBuff):
    """
        BuffAtkOutPer - 兵刃伤害buff百分比
    """

    def __init__(self, src, zfindex: int, dest, lastturns: int, atkoutper: float):
        """
            构造函数
        """

        super().__init__("atkoutper", src, zfindex, dest, lastturns)

        self.atkOutPer = atkoutper

    def merge(self, _buff):
        """
            merge - 2个同类状态需要处理，加减统率不能叠加，必须全部都保留
        """
        return False

    def onMerge(self, _buff) -> bool:
        """
            onMerge - 叠加，加减兵刃伤害不能叠加，必须全部都保留
        """
        return False

    def inSnapshot(self, statusSnapshot) -> bool:
        """
            inSnapshot - 是否应该保留进快照里
                如果是发出兵刃攻击，则需要保留
        """

        if statusSnapshot.typecode == 'atkout':
            statusSnapshot.atkOutPer += self.atkOutPer

            return True

        return False
