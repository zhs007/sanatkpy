# -*- coding:utf-8 -*-
"""
    status - 状态，一组Buff的组合
"""

# pylint: disable = invalid-name
# pylint: disable = line-too-long


class Status:
    """
        Status - 状态，一组Buff的组合
    """

    def __init__(self):
        """
            构造函数
        """

        self.lstBuff = []

    def addBuff(self, buff):
        """
            addBuff - 附加一个新的Buff
        """

        for _, v in enumerate(self.lstBuff):
            if v.isSame(buff):
                v.merge(buff)

                return

        self.lstBuff.append(buff)

    def canImmunity(self, dest):
        """
            canImmunity - 是否可以免疫这种buff
        """

        for _, v in enumerate(self.lstBuff):
            if v.canImmunity(dest):
                return True

        return False

    def hasBuff(self, code):
        """
            hasBuff - 是否有这个Buff
        """

        for _, v in enumerate(self.lstBuff):
            if v.code == code:
                return True

        return False
