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

        for i in range(len(self.lstBuff)):
            if self.lstBuff[i].isSame(buff):
                self.lstBuff[i].merge(buff)

                return

        self.lstBuff.append(buff)
