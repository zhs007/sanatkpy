# -*- coding:utf-8 -*-
"""
    buffdef - Buffdef 防御buff
"""
from sanatkpy.buff import BaseBuff
# pylint: disable = invalid-name
# pylint: disable = line-too-long


class BuffDef(BaseBuff):
    """
        BuffDef - 统率，加减统率，非百分比
    """

    def __init__(self, srcindex: int, zfindex: int, destindex: int, lastturns: int, isHL: bool, defval: int):
        """
            构造函数
        """

        super().__init__("def", srcindex, zfindex, destindex, lastturns, isHL)

        self.defVal = defval

    def merge(self, buff):
        """
            merge - 2个同类状态需要处理，加减统率不能叠加，必须全部都保留
        """
        return False

    def onMerge(self, _buff) -> bool:
        """
            onMerge - 叠加，加减统率不能叠加，必须全部都保留
        """
        return False

    def inSnapshot(self, statusSnapshot) -> bool:
        """
            inSnapshot - 是否应该保留进快照里
                如果是受到兵刃攻击，则需要保留
        """

        if statusSnapshot.typecode == 'atkin':
            statusSnapshot.defOff += self.defVal

            return True

        return False
