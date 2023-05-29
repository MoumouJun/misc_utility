#!/usr/bin/env python3
# -*- coding: UTF-8


from base import *
import influxdb

# 20230525 14:00:00
syslog_time_format = "%Y%m%d %H:%M:%S"

# 日志时间转为时序数据库格式时间

"""
1. 以日志最新时间为基准，处理基准时间的上一秒日志
2.
"""


def exec_sh(cmd: str) -> tuple[int, str]:
    return subprocess.getstatusoutput(cmd)


def logT2tsdbT():
    pass


def get_time_by_format(format: str = syslog_time_format) -> str:
    '''通过指定格式获取最新的时间'''
    return ("{}".format(time.strftime(
        format, time.localtime(time.time()))))


def wait_Sec_change(stamp):
    '''等待秒数发生变化'''
    curr = stamp
    while True:
        if curr != stamp:
            print("当前时间:{}".format(time.strftime(
                syslog_time_format, time.localtime(stamp))))
            break
        time.sleep(0.1)
        stamp = math.floor(time.time())


class CLogPaser(CBaseObject):
    def __init__(self) -> None:
        super(CLogPaser, self).__init__()
        self._tsdb = influxdb.influx_oper()
        print(dir(influxdb))
        self._t_parse = get_time_by_format()  # 当前处理到了哪一秒
        self._t_stamp = time.time()  # unix时间戳
        self._cfg = json5.load(open('./logParse_cfg.json'))

        self._record = influxdb.influx_record()
        self._record_l = []  # 待写入的数据
        print(self._cfg)

    def _init_log_parse_cfg(self, cfg_json='./logParse_cfg.json'):
        pass

    def _parse_syslog(self):
        self._record_l.clear()
        self._t_parse = '2023-05-25'
        # self._t_parse = '20230525 14:00:01'
        for k, v in self._cfg['syslog']['module'].items():
            if 'file' not in v.keys():
                continue
            # 1 获取日志
            rtn, out = exec_sh("grep '{0}' {1}".format(
                self._t_parse, v['file']))
            print("log_row_info[{0}]".format(out))
            # 2 解析日志
            # 2.1 row
            self._record.set(k, 'module', 'row',
                             self._t_parse, {'content': out})

            # 更新record
            self._record_l.append(self._record)

    def _flush(self):
        '''将数据写入时序数据库'''
        for i in self._record_l:
            self._tsdb.write(i)
        self._record_l.clear()

    def test(self):
        while True:
            wait_Sec_change(math.floor(time.time()))
            self._parse_syslog()
            self._flush()
            # f =

    def _paser_syslog_base(self):
        '''解析日志基础信息'''
        pass

    # --------------------------------------------------------------------------
    # 与时序数据库交互

    def _write_record(self):
        pass


if __name__ == '__main__':
    CLogPaser().test()
