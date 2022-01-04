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

    def clear(self):
        """
            clear - clear
        """

        self.lstBuff = []

    def addBuff(self, buff) -> int:
        """
            addBuff - 附加一个新的Buff

            Returns:
                1 表示已经附加
                0 表示冲突
                -1 表示免疫
        """

        if self.canImmunity(buff):
            return -1

        #! 这里还应该处理不能合并的情况，需要返回False

        for _, v in enumerate(self.lstBuff):
            if v.isSame(buff):
                if v.merge(buff):
                    return 1

        self.lstBuff.append(buff)

        #! 这里还应该处理新buff可以免疫已存在buff的情况

        return 1

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

    def canBaseAttack(self, src):
        """
            canBaseAttack - 是否可以普通攻击
        """

        for _, v in enumerate(self.lstBuff):
            if not v.canBaseAttack(src):
                return False

        return True

    def canZDSkill(self, src):
        """
            canZDSkill - 是否可以释放主动战法
        """

        for _, v in enumerate(self.lstBuff):
            if not v.canZDSkill(src):
                return False

        return True
