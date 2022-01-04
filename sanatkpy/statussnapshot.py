# -*- coding:utf-8 -*-
"""
    statussnapshot - 状态快照，可选保存哪一部分
"""

# pylint: disable = invalid-name
# pylint: disable = line-too-long


class StatusSnapshot:
    """
        StatusSnapshot - 状态快照，可选保存哪一部分
    """

    def __init__(self, typecode: str, status):
        """
            构造函数
        """

        self.typecode = typecode
        self.atkOff = 0
        self.defOff = 0
        self.atkPer = 0
        self.defPer = 0
        self.magicOff = 0
        self.magicPer = 0
        self.speedOff = 0
        self.speedPer = 0
        # self.lstBuff = []

        self._build(status)

    def _build(self, status) -> None:
        """
            _build - 生成一个快照，兵刃攻击相关
        """

        # self.lstBuff = []

        for _, v in enumerate(status.lstBuff):
            v.inSnapshot(self)
