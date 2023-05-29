#!/usr/bin/env python3
# -*- coding: UTF-8

from influxdb import *
import datetime

Table = "aaa2"


def parse_row(row: OrderedDict):
    p=Point(Table) \
    .tag("type", "vix-daily") \
    .field("open", float(row['VIX Open'])) \
    .field("high", float(row['VIX High'])) \
    .field("low", float(row['VIX Low'])) \
    .field("close", float(row['VIX Close'])) \
    .time("{0:.19}{1}".format(str(datetime.datetime.now()), 'Z-8'))
    print(p.to_line_protocol())
    return p


data = rx \
    .from_iterable(DictReader(open('./test.csv', 'r'))) \
    .pipe(ops.map(lambda row: parse_row(row)))

with InfluxDBClient(url=INFLUXDB2_CFG['url'], token=INFLUXDB2_CFG['token'], org=INFLUXDB2_CFG['org'], debug=True) as client:

    """
    Create client that writes data in batches with 50_000 items.
    """
    with client.write_api(write_options=WriteOptions(batch_size=50_000, flush_interval=10_000)) as write_api:
        write_api.write(bucket="test", record=data)

    """
    Querying max value of CBOE Volatility Index
    """
    query = 'from(bucket:"test")' \
            ' |> range(start: 0, stop: now())' \
            ' |> filter(fn: (r) => r._measurement == "{0}")' \
            ' |> timeShift(duration: 8h)'.format(Table)
    result = client.query_api().query(query=query)

    """
    Processing results
    """
    print()
    print("=== results ===")
    print()
    for table in result:
        print(table)
        for record in table.records:
            print(record)
            print('max {0:5} = {1}'.format(
                record.get_field(), record.get_value()))
