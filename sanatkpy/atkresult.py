# -*- coding:utf-8 -*-

# newResult - new a result
def newResult():
    return {
        'mnatk': 0,             # 谋略伤害，百分比
        'atk': 0,               # 兵刃伤害，百分比
        'zl': 0,                # 治疗，百分比
        'fireLastTurns': 0,     # 灼烧状态剩余回合
        'waterLastTurns': 0,    # 水攻状态剩余回合
        'noBAtkLastTurns': 0,   # 缴械状态剩余回合，无法进行普通攻击
        'weakLastTurns': 0,     # 虚弱状态剩余回合，无法造成伤害
        'noZDLastTurns': 0,     # 技穷状态剩余回合，无法发动主动技能
    }
