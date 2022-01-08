# -*- coding:utf-8 -*-
"""
    utils - utils
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long


def isSameArmy(srcindex: int, destindex: int) -> bool:
    """
    isSameArmy - 是否是同一边
    """

    assert srcindex >= 0 and srcindex < 6
    assert destindex >= 0 and destindex < 6

    if srcindex < 3:
        return destindex < 3

    return destindex >= 3


def isMainGeneral(myindex: int) -> bool:
    """
    isMainGeneral - 是否是主将
    """

    assert myindex >= 0 and myindex < 6

    return myindex == 0 or myindex == 3


def toPersentString(val: float) -> str:
    """
    toPersentString - 返回百分比字符串
    """

    return f"{int(val * 100)}%"
