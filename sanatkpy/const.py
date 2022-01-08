# -*- coding:utf-8 -*-
"""
    const - ConstValue
"""
# pylint: disable = invalid-name
# pylint: disable = line-too-long


class ConstValue(object):
    """
    ConstValue - const
    """

    class ConstError(TypeError):
        """
        ConstError - ConstError
        """

    class ConstCaseError(ConstError):
        """
        ConstCaseError - ConstCaseError
        """

    def __setter__(self, name, value):
        """
        __setter__ - __setter__
        """

        if name in self.__dict__:
            value = name
            raise self.ConstError(f"Not allowed change const. {value}")

        if not name.isupper():
            value = name
            raise self.ConstCaseError(f"Const's name is not all uppercase. {value}")

        self.__dict__[name] = value


ConstValue.ZDZF = "zdzf"  # 主动战法
ConstValue.TJZF = "tjzf"  # 突击战法
ConstValue.ZHZF = "zhzf"  # 指挥战法
ConstValue.BDZF = "bdzf"  # 被动战法
ConstValue.BASEATK = "baseatk"  # 普通攻击

ConstValue.ZFLEVEL_S = "A"  # S
ConstValue.ZFLEVEL_A = "A"  # A
ConstValue.ZFLEVEL_B = "B"  # B
ConstValue.ZFLEVEL_N = "N"  # BaseAtk
