# -*- coding:utf-8 -*-

class Status:
    def __init__(self):
        self.lstBuff = []

    def addBuff(self, buff):
        for i in range(len(self.lstBuff)):
            if self.lstBuff[i].isSame(buff):
                self.lstBuff[i].merge(buff)
                
                return

        self.lstBuff.append(buff)