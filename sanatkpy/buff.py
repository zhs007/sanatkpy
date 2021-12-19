# -*- coding:utf-8 -*-

class DefBuff:
    def __init__(self, srcindex: int, zfindex: int, defper: float, lastturns: int, isHL: bool):
        self.dfIndex = zfindex              # 阵法索引
        self.srcIndex = srcindex            # 来源
        self.defPer = defper                # 造成的减防或增防
        self.lastTurns = lastturns          # 剩余回合数
        self.isHL = isHL                    # 是否是自己人造成的减防或敌人造成的增防
