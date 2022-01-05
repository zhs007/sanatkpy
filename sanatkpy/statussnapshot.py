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
        self.atkOff = 0     # 武力
        self.defOff = 0     # 统率
        self.atkPer = 0     # 武力百分比
        self.defPer = 0     # 统率百分比
        self.magicOff = 0   # 谋略
        self.magicPer = 0   # 谋略百分比
        self.speedOff = 0   # 速度
        self.speedPer = 0   # 速度百分比
        self.atkInPer = 0   # 受到兵刃伤害百分比
        self.atkOutPer = 0  # 造成兵刃伤害百分比

        self._build(status)

    def _build(self, status) -> None:
        """
            _build - 生成一个快照，兵刃攻击相关
        """

        # self.lstBuff = []

        for _, v in enumerate(status.lstBuff):
            v.inSnapshot(self)
