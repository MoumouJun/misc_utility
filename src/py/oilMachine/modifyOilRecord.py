#!/usr/bin/python3


f_src = open("./modifyOilRecord.log")
f_dst = open("oilRecord.new.log", mode="w+")
record_eg = "BB 02 2D 41 00 01 23 00 08 03 06 53 00 6C 20 12 12 16 50 35 76 34 1F 64 D6 BD 22 64 00 12 6C 29 00 00 09 67 60 09 00 00 00 46 88 41 3A DC"


class OilRecord(object):
    def __init__(self, record: str) -> None:
        str_len = len(record)
        if str_len != 138 and str_len != 137:
            print("加油记录字符串长度实际为[%s],应为[138]或[137],例如:%s" %
                  (str_len, record_eg))
        self._record_str = record
        self._time = ""
        self._seqno = 0
        self._total = 0.0
        self._gun = 0  # 油枪号
        self._money = 0.0  # 加油金额
        self._volume = 0.0  # 加油量
        self._unit = 0.0  # 单价
        self.updRecord()

    def _formattime(self, t: str = "221006174238") -> str:
        time = ("%s-%s-%s %s:%s:%s" % (
            t[0:][:2], t[2:][:2], t[4:][:2], t[6:][:2], t[8:][:2], t[10:][:2],
        ))
        return time

    def updRecord(self):
        self._time = self._formattime(self._record_str[42:].replace(" ", ""))
        self._gun = int(self._record_str[3:][:2])
        self._seqno = int("0x"+self._record_str[36:][:2], 16) + \
            int("0x"+self._record_str[39:][:2], 16)
        self._total = float(
            int(self._record_str[97:][:12].replace(" ", ""))+int(self._record_str[109:][:2])/100)

    def _isRight(self, new_total: float = 0) -> bool:
        '''当前这一笔加油记录是否正确'''
        if new_total != self._volume+self._total:
            return False
        return True

    def show(self):
        print("枪号[%s],序号[%s],时间[%s],累积量[%s]"
              % (self._gun, self._seqno, self._time, self._total))


for i in f_src.readlines():
    print(i.replace("\n", ""))
    record = OilRecord(i.replace("\n", ""))
    record.show()
