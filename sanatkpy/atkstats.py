# -*- coding:utf-8 -*-
"""
    atkstats - 战斗统计
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long


class AtkStats:
    """
        AtkStats - 战斗统计
    """

    def __init__(self, myindex: int, zfindex: int):
        """
            __init__ - 构造函数
        """

        self.myindex = myindex
        self.zfindex = zfindex
        self.atkOutTotal = 0                    # 造成的兵刃总伤害
        self.atkOut = [0, 0, 0, 0, 0, 0]        # 造成的兵刃伤害
        self.atkIn = [0, 0, 0, 0, 0, 0]         # 得到的兵刃伤害
