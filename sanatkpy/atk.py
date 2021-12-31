# -*- coding:utf-8 -*-
# pylint: disable = invalid-name
# pylint: disable = line-too-long

from sanatkpy.atkresult import AtkResult
from sanatkpy.general import General


def simAttack(funcZF, myindex: int, zfindex: int, turnNums: int):
    ret = AtkResult()

    for curturn in range(1, turnNums+1):
        funcZF(ret, myindex, zfindex, curturn)

    return ret
