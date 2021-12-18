# -*- coding:utf-8 -*-

class DefBuff:
    def __init__(self, srcindex: int, zfindex: int, defper: float, lastturns: int):
        self.dfIndex = zfindex              # 阵法索引
        self.srcIndex = srcindex            # 来源
        self.defPer = defper                # 造成的减防或增防
        self.lastTurns = lastturns          # 剩余回合数