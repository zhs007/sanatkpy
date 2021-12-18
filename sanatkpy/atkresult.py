# -*- coding:utf-8 -*-
import random
from sanatkpy.general import General
from sanatkpy.buff import DefBuff


class AtkResult:
    def __init__(self):
        self.mnatk = 0              # 谋略伤害，百分比
        self.atk = 0                # 兵刃伤害，百分比
        self.zl = 0                 # 治疗，百分比
        self.fireLastTurns = 0      # 灼烧状态剩余回合
        self.waterLastTurns = 0     # 水攻状态剩余回合
        self.noBAtkLastTurns = 0    # 缴械状态剩余回合，无法进行普通攻击
        self.weakLastTurns = 0      # 虚弱状态剩余回合，无法造成伤害
        self.noZDLastTurns = 0      # 技穷状态剩余回合，无法发动主动技能

        self.enemy = [General(), General(), General()]
        self.our = [General(), General(), General()]

    def clear(self):
        self.mnatk = 0              # 谋略伤害，百分比
        self.atk = 0                # 兵刃伤害，百分比
        self.zl = 0                 # 治疗，百分比
        self.fireLastTurns = 0      # 灼烧状态剩余回合
        self.waterLastTurns = 0     # 水攻状态剩余回合
        self.noBAtkLastTurns = 0    # 缴械状态剩余回合，无法进行普通攻击
        self.weakLastTurns = 0      # 虚弱状态剩余回合，无法造成伤害
        self.noZDLastTurns = 0      # 技穷状态剩余回合，无法发动主动技能

        for i in range(3):
            self.enemy[i].clear()
            self.our[i].clear()

    def genEmenyIndex(self, myindex: int, isHL: bool):
        if isHL:
            arr = [1, 2, 3]
            for i in range(3):
                if i != myindex:
                    arr.append(-(i + 1))

            ri = int(random.random() * 5)
            return arr[ri]
        else:
            ri = int(random.random() * 3)

            return ri + 1

    # destindex - [-3, 3]
    def addAttack(self, myindex: int, destindex: int, atk: float):
        myinfo = self.our[myindex]

        if destindex > 0:
            destinfo = self.enemy[destindex - 1]

            self.atk += atk

            myinfo.atkOutTotal += atk
            myinfo.atkOut[destindex - 1] += atk

            destinfo.atkIn[myindex] += atk
        else:
            destinfo = self.our[-destindex - 1]
            srcinfo = self.enemy[myinfo.HLSrc]

            destinfo.atkIn[myinfo.HLSrc] += atk
            srcinfo.HLAtk[myindex] += atk

    # destindex - [-3, 3]
    def addStatusJX(self, myindex: int, destindex: int, turns: int):
        myinfo = self.our[myindex]

        if destindex > 0:
            destinfo = self.enemy[destindex - 1]

            if destinfo.noBAtkLastTurns == 0:
                destinfo.noBAtkLastTurns = turns
                self.noBAtkLastTurns += turns
        else:
            destinfo = self.our[-destindex - 1]

            if destinfo.noBAtkLastTurns == 0:
                destinfo.noBAtkLastTurns = turns
                self.noBAtkLastTurns += turns            

    # destindex - [-3, 3]
    def addStatusJQ(self, myindex: int, destindex: int, turns: int):
        myinfo = self.our[myindex]
        destinfo = self.enemy[destindex]

        if destinfo.noZDLastTurns == 0:
            destinfo.noZDLastTurns = turns
            self.noZDLastTurns += turns

    # destindex - [-3, 3]
    def addEnemyDownDef(self, myindex: int, destindex: int, zfindex: int, defper: float, turns: int):
        myinfo = self.our[myindex]
        destinfo = self.enemy[destindex]

        destinfo.addDefBuff(myindex, zfindex, defper, turns)

    # destindex - [-3, 3]
    def addInDef(self, myindex: int, destindex: int, zfindex: int, defper: float, turns: int):
        myinfo = self.our[myindex]
        destinfo = self.enemy[destindex]

        destinfo.addDefBuff(myindex, zfindex, defper, turns)
