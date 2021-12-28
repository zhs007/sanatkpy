# -*- coding:utf-8 -*-

class AtkReportLine:
    def __init__(self, txt, meta: dict):
        self.txt = txt
        self.meta = meta

    def genString(self):
        arr = self.txt.split('#')
        if len(arr) == 1:
            return arr[0]

        if len(arr) < 3:
            return self.txt

        output = ''
        for i in range(len(arr)):
            if i % 2 == 1:
                if self.meta != None and arr[i] in self.meta.keys():
                    output += self.meta[arr[i]]
            else:
                output += arr[i]

        return output


class AtkReportParagraph:
    def __init__(self, paragraphname):
        self.paragraphName = paragraphname
        self.lstLine = []

    def addLine(self, txt, meta):
        self.lstLine.append(AtkReportLine(txt, meta))


class AtkReportPart:
    def __init__(self, partname):
        self.partName = partname
        self.lstParagraph = []

    def addParagraph(self, paragraphname):
        self.lstParagraph.append(AtkReportParagraph(paragraphname))

    def findParagraph(self, paragraphname):
        for i in range(len(self.lstParagraph)):
            if paragraphname == self.lstParagraph[i].paragraphName:
                return i

        return -1

    def addLine(self, paragraphname, txt, meta):
        i = self.findParagraph(paragraphname)
        if i >= 0:
            self.lstParagraph[i].addLine(txt, meta)


class AtkReport:
    def __init__(self):
        self.lstPart = []

    def addPart(self, partname):
        self.lstPart.append(AtkReportPart(partname))

    def findPart(self, partname):
        for i in range(len(self.lstPart)):
            if partname == self.lstPart[i].partName:
                return i

        return -1

    def addParagraph(self, partname, paragraphname):
        i = self.findPart(partname)
        if i >= 0:
            self.lstPart[i].addParagraph(paragraphname)

    def addLine(self, partname, paragraphname, txt, meta):
        i = self.findPart(partname)
        if i >= 0:
            self.lstPart[i].addLine(paragraphname, txt, meta)

    def genString(self):
        output = ''

        for i in range(len(self.lstPart)):
            output += self.lstPart[i].partName
            output += '\n'

            for j in range(len(self.lstPart[i].lstParagraph)):
                output += '\t'
                output += self.lstPart[i].lstParagraph[j].paragraphName
                output += '\n'

                for k in range(len(self.lstPart[i].lstParagraph[j].lstLine)):
                    output += '\t\t'
                    output += self.lstPart[i].lstParagraph[j].lstLine[k].genString()
                    output += '\n'
