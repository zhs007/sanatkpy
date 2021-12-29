# -*- coding:utf-8 -*-
import sys 
sys.path.append("..")
import sanatkpy

report = sanatkpy.AtkReport()

report.addPart("准备")
report.addPart("回合一")
report.addParagraph("准备", "士气", "#team# 士气为 #sq# ，伤害调整为 #allatk#% 。",
                    {
                        'team': '关羽队',
                        'sq': 50,
                        'allatk': 100 - 35,
                    })
report.addParagraph("回合一", "关羽开始行动", "#general# 开始行动",
                    {
                        'general': '关羽',
                    })
report.addLine("回合一", "关羽开始行动", "#general# 发动 #skill# 。", {
    'general': '关羽',
    'skill': '威震华夏',
})

strReport = report.genString()

print(strReport)
