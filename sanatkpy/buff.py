# -*- coding:utf-8 -*-
"""
    buff - Buff
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long


# class DefBuff:
#     """
#         DefBuff - 防御Buff
#     """

#     def __init__(self, srcindex: int, zfindex: int, defper: float, lastturns: int, isHL: bool):
#         """
#             构造函数
#         """

#         self.dfIndex = zfindex              # 阵法索引
#         self.srcIndex = srcindex            # 来源
#         self.defPer = defper                # 造成的减防或增防
#         self.lastTurns = lastturns          # 剩余回合数
#         self.isHL = isHL                    # 是否是自己人造成的减防或敌人造成的增防


class BaseBuff:
    """
        BaseBuff - Buff基类
    """

    def __init__(self, code: str, srcindex: int, zfindex: int, destindex: int, lastturns: int, isHL: bool):
        """
            构造函数
        """

        # 静态属性
        self.code = code

        # 动态属性
        self.srcIndex = srcindex
        self.zfIndex = zfindex
        self.destIndex = destindex
        self.lastTurns = lastturns
        self.isHL = isHL

    def onTurns(self):
        """
            onTurns - 每个回合开始调用
        """
        if self.lastTurns > 0:
            self.lastTurns -= 1

    def isSame(self, buff):
        """
            isSame - 是否是同类Buff
        """
        return self.code == buff.code

    def merge(self, buff) -> bool:
        """
            merge - 2个同类状态需要处理，返回True表示已经处理完了，返回False表示无法merge，只能添加
        """
        if self.code == buff.code:
            return self.onMerge(buff)

        return False

    def onMerge(self, _buff) -> bool:
        """
            onMerge - 具体的合成方式，返回True表示已经处理完了，返回False表示无法merge，只能添加
        """
        return False

    def canBaseAttack(self, _src):
        """
            canBaseAttack - 是否可以普通攻击
        """

        return True

    def canImmunity(self, _dest):
        """
            canImmunity - 是否可以免疫这种buff
        """

        return False

    def canZDSkill(self, _src):
        """
            canZDSkill - 是否可以释放主动战法
        """

        return True

    def inSnapshot(self, _statusSnapshot) -> bool:
        """
            isInSnapshot - 是否应该保留进快照里
        """

        return False
