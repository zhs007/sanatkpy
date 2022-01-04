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

    def __init__(self, srcindex: int, zfindex: int, destindex: int, lastturns: int, isHL: bool):
        """
            构造函数
        """

        super().__init__("hl", srcindex, zfindex, destindex, lastturns, isHL)

    def onMerge(self, _buff) -> bool:
        """
            onMerge - 抛弃掉新buff
        """
        return True
