# -*- coding:utf-8 -*-
import sys

sys.path.append("..")
import sanatkpy

lstgeneral0 = [
    sanatkpy.General(0, "关羽"),
    sanatkpy.General(1, "不重要友军1"),
    sanatkpy.General(2, "不重要友军2"),
]
lstgeneral1 = [
    sanatkpy.General(3, "不重要敌军1"),
    sanatkpy.General(4, "不重要敌军2"),
    sanatkpy.General(5, "不重要敌军3"),
]

lstgeneral0[0].addZF(0, sanatkpy.WZHX(lstgeneral0[0], 0))

ret = sanatkpy.simAttack2(lstgeneral0, lstgeneral1, 8)
print(ret.report.genString())
