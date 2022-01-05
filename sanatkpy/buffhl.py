# -*- coding:utf-8 -*-
"""
    buffhl - BuffHL 混乱
"""
from sanatkpy.buff import BaseBuff
# pylint: disable = invalid-name
# pylint: disable = line-too-long


class BuffHL(BaseBuff):
    """
        BuffHL - 混乱
    """

    def __init__(self, src, zfindex: int, dest, lastturns: int):
        """
            构造函数
        """

        super().__init__("hl", src, zfindex, dest, lastturns)

    def onMerge(self, _buff) -> bool:
        """
            onMerge - 抛弃掉新buff
        """
        return True
