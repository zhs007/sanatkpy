# -*- coding:utf-8 -*-
"""
    atkreport - 战报
"""

# pylint: disable = invalid-name
# pylint: disable = line-too-long


class AtkReportLine:
    """
    AtkReportLine - 战报行数据，字符串数据拼接
    """

    def __init__(self, txt, meta: dict):
        """
        构造函数
        """
        self.txt = txt
        self.meta = meta

    def genString(self):
        """
        genString - 生成字符串
        """

        arr = self.txt.split("#")
        if len(arr) == 1:
            return arr[0]

        if len(arr) < 3:
            return self.txt

        output = ""
        for i, v in enumerate(arr):
            if i % 2 == 1:
                if self.meta is not None and v in self.meta.keys():
                    output += str(self.meta[v])
            else:
                output += v

        return output


class AtkReportParagraph:
    """
    AtkReportParagraph - 战报段落数据，某个武将的一次完整行动
    """

    def __init__(self, paragraphname, maintxt, mainmeta):
        """
        构造函数
        """
        self.paragraphName = paragraphname
        self.mainLine = AtkReportLine(maintxt, mainmeta)
        self.lstLine = []

    def addLine(self, txt, meta):
        """
        addLine - 为这个段落增加一行战报
        """
        self.lstLine.append(AtkReportLine(txt, meta))


class AtkReportPart:
    """
    AtkReportPart - 战报大区数据，准备阶段、回合一阶段等
    """

    def __init__(self, partname):
        """
        构造函数
        """
        self.partName = partname
        self.lstParagraph = []

    def addParagraph(self, paragraphname, maintxt, mainmeta):
        """
        addParagraph - 为这个战报区增加一个段落
        """
        self.lstParagraph.append(AtkReportParagraph(paragraphname, maintxt, mainmeta))

    def findParagraph(self, paragraphname):
        """
        findParagraph - 找到一个段落，返回-1表示没找到
        """
        for i, v in enumerate(self.lstParagraph):
            if paragraphname == v.paragraphName:
                return i

        return -1

    def addLine(self, paragraphname, txt, meta):
        """
        addLine - 增加一行
        """
        i = self.findParagraph(paragraphname)
        if i >= 0:
            self.lstParagraph[i].addLine(txt, meta)


class AtkReport:
    """
    AtkReport - 战报
    """

    def __init__(self):
        """
        构造函数
        """
        self.lstPart = []

        self.curpart = -1
        self.curparagraph = -1

    def addPart(self, partname):
        """
        addPart - 增加一个Part
        """

        self.lstPart.append(AtkReportPart(partname))
        self.curpart = len(self.lstPart) - 1

    def findPart(self, partname):
        """
        findPart - 查找一个Part
        """

        for i, v in enumerate(self.lstPart):
            if partname == v.partName:
                return i

        return -1

    def addParagraph(self, partname, paragraphname, maintxt, mainmeta):
        """
        addParagraph - 增加一个 paragraph
        """

        i = self.findPart(partname)
        if i >= 0:
            self.curpart = i
            self.lstPart[i].addParagraph(paragraphname, maintxt, mainmeta)
            self.curparagraph = len(self.lstPart[i].lstParagraph) - 1

    def addParagraphEx(self, paragraphname, maintxt, mainmeta):
        """
        addParagraph - 增加一个 paragraph
        """

        if self.curpart >= 0:
            self.lstPart[self.curpart].addParagraph(paragraphname, maintxt, mainmeta)
            self.curparagraph = len(self.lstPart[self.curpart].lstParagraph) - 1

    def addLine(self, partname, paragraphname, txt, meta):
        """
        addLine - 增加一个 line
        """

        i = self.findPart(partname)
        if i >= 0:
            self.lstPart[i].addLine(paragraphname, txt, meta)

    def addLineEx(self, txt, meta):
        """
        addLine - 增加一个 line
        """

        if self.curpart >= 0 and self.curparagraph >= 0:
            self.lstPart[self.curpart].lstParagraph[self.curparagraph].addLine(
                txt, meta
            )

    def genString(self) -> str:
        """
        genString - 生成一个完整的战报
        """

        output = ""

        for _, part in enumerate(self.lstPart):
            output += part.partName
            output += "\n"

            for _, paragraph in enumerate(part.lstParagraph):
                output += "\t"
                output += paragraph.mainLine.genString()
                output += "\n"

                for _, line in enumerate(paragraph.lstLine):
                    output += "\t\t"
                    output += line.genString()
                    output += "\n"

        return output
