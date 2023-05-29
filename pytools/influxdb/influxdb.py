#!/usr/bin/env python3
# -*- coding: UTF-8

from base import *
import env
from reactivex import operators as ops
import reactivex as rx
from csv import DictReader
from collections import OrderedDict

from influxdb_client import InfluxDBClient, client, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS


import sys
sys.path.append('/home/liujun/misc_utility/pytools/')


INFLUXDB2_CFG = {
    'url': 'http://127.0.0.1:8086/',
    'org': 'liujun',
    'bucket': 'test',  # 类似于数据库名称
    'token':  '9oKEsEgfe8vgMYuAmZhcto60JBj4Wdyw_9eCc53dNkESCcoS-SLfZfB9DT60hjPsRMzDvO_EBA_h041teZuErw=='
    # _measurement 类似于表名
    # tag k-v 可作为索引
    # field  k-v 常规字段
}


def utc2beijing(self, utc_time: str) -> str:
    '''utc时间转为北京时间，相差八小时'''
    pass


def get_utc(t='2023-05-29T17:38:16Z', format='%Y-%m-%dT%H:%M:%SZ'):
    '''获取utd时间'''
    # "{0:.19}{1}".format(str(datetime.datetime.now()),'Z-8')
    #
    t_ = time.strptime(t, format)
    return datetime.datetime(t_)


class influx_record(object):
    def __init__(self, table: str = '', tag_lable: str = '', tag_name: str = '', time: str = '', fields: dict = {}):
        self.table: str = table
        self.tag_lable: str = tag_lable
        self.tag_name: str = tag_name
        self.time: str = time
        self.fields: dict = fields
        self._point: Point = self.genPoint()

    def genPoint(self) -> Point:
        p = Point(self.table)\
            .tag(self.tag_lable, self.tag_name)\
            .time(self.time+'Z-8', "s")
        for k, v in self.fields.items():
            p.field(k, v)
        return p

    def set(self, table: str, tag_lable: str, tag_name: str, time: str, fields: dict):
        self.table = table
        self.tag_lable = tag_lable
        self.tag_name = tag_name
        self.time = time
        self.fields = fields
        self._point = self.genPoint()

    def get(self):
        self.show()
        return self._point

    def show(self):
        print("table[{0}],tag_lable[{1}],tag_name[{2}],time[{3}],fields[{4}]".format(
            self.table, self.tag_lable, self.tag_name, self.time, self.fields))
        print('Point[{0}]'.format(self._point.to_line_protocol()))

    def reset(self):
        self.__init__()


class influx_oper(CBaseObject):
    def __init__(self) -> None:
        super(influx_oper, self).__init__()
        db_client = InfluxDBClient(
            url=INFLUXDB2_CFG['url'], token=INFLUXDB2_CFG['token'], org=INFLUXDB2_CFG['org'])
        self._db_write = db_client.write_api(
            write_options=SYNCHRONOUS)
            # write_options=WriteOptions(batch_size=50_000, flush_interval=10_000))
        self._db_del = db_client.delete_api()
        self._db_qry = db_client.query_api()
        self._qry = ""  # 查询语句

    # --------------------------------------------------------------------------
    # utility

    # --------------------------------------------------------------------------
    # 基础接口：增查删
    def _show_Point(self, Point):
        print("")

    def _write(self, record_: Point):
        print("tsdb写库:{}".format(record_.to_line_protocol()))
        out = self._db_write.write(
            INFLUXDB2_CFG['bucket'], INFLUXDB2_CFG['org'], record=record_)
        if out != None and out != "":
            print("tsdb写库:{}".format(out))
        return out

    # --------------------------------------------------------------------------
    # 扩展接口：增查删

    def write(self, record: influx_record):
        '''写一条数据'''
        rtn = self._write(record.get())
    # def write(self, table, tag_lable, tag_name, time, fields: dict):
    #     '''写一条数据'''
    #     p = Point(table).tag(tag_lable, tag_name).time(time)
    #     for k, v in fields.items():
    #         p.field(k, v)
    #     rtn = self._write(p)

    def delete_table(self, table: str):
        '''删除{table}表内所有数据，如果表明指定为"",则删除所有表'''
        return self._db_del.delete(start=datetime.datetime.utcfromtimestamp(0),
                                   stop=datetime.datetime.now(),
                                   predicate=f'_measurement="{table}"',
                                   bucket=INFLUXDB2_CFG['bucket'],
                                   org=INFLUXDB2_CFG['org'])

    def find(self, table, start="", stop="", last="", tags: dict = {}, fields: list = []):
        '''查找数据
            :查找顺序
             :last
             :start -> now()
             :0 -> stop
        '''
        self._qry = 'from(bucket:"test")|> filter(fn: (r) => r._measurement == "{0}")'.format(
            table)
        if last != "":
            self._qry = self._qry+' |> range(start: 0, stop: now())'
        elif start == "" and stop == "":
            self._qry = self._qry + ' |> range(start: 0, stop: now())'
        elif fields != {}:
            s = ""
            for i in fields:
                s = s+'or r["_field"] == "{0}"'.format(i)
            s.removeprefix('or')
            self._qry = self._qry + '|> filter(fn: (r) => {0})'.format(s)

        self._qry = self._qry + '|> timeShift(duration: 8h)'
        return self._db_qry.query(query=self._qry)


if __name__ == '__main__':
    log = '20230528 15:00:03 tradetest2 tkernel_1.sub [12345]: OrderInsert[123456], QrderInsertTotal[7654321]'
    record = influx_record('tkernel', 'syslog', 'row',
                           '20230528 15:00:06', {'row1': log})
    db = influx_oper()
    db.write(record)
    # db.delete_table('aaa')
    # tl = db.find(table='aaa')
    # for i in tl:
    #     print(i)
    #     for record in i.records:
    #         print(record)
    #         print(record.get_field())
