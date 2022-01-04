# -*- coding:utf-8 -*-
"""
    status - 状态，一组Buff的组合
"""

# pylint: disable = invalid-name
# pylint: disable = line-too-long
from sanatkpy.statussnapshot import StatusSnapshot


class Status:
    """
        Status - 状态，一组Buff的组合
    """

    def __init__(self):
        """
            构造函数
        """

        self.lstBuff = []

    def addBuff(self, buff) -> None:
        """
            addBuff - 附加一个新的Buff
        """

        for _, v in enumerate(self.lstBuff):
            if v.isSame(buff):
                if v.merge(buff):
                    return

        self.lstBuff.append(buff)

    def canImmunity(self, dest) -> bool:
        """
            canImmunity - 是否可以免疫这种buff
        """

        for _, v in enumerate(self.lstBuff):
            if v.canImmunity(dest):
                return True

        return False

    def hasBuff(self, code) -> bool:
        """
            hasBuff - 是否有这个Buff
        """

        for _, v in enumerate(self.lstBuff):
            if v.code == code:
                return True

        return False

    def findBuff(self, code) -> int:
        """
            findBuff - 是否有这个Buff
        """

        for i, v in enumerate(self.lstBuff):
            if v.code == code:
                return i

        return -1

    def genSnapshot(self, typecode) -> StatusSnapshot:
        """
            findBuff - 是否有这个Buff
        """

        return StatusSnapshot(typecode, self)
