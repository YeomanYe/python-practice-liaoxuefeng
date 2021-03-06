# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
	dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
	re_comp = re.compile(r'UTC([+-][\d]*?)(:00)')
	tz_num = int(re_comp.match(tz_str).group(1))
	tz_utc = timezone(timedelta(hours=tz_num))
	dt_utc = dt.replace(tzinfo=tz_utc)
	print(dt_utc)
	return dt_utc.timestamp()


# 测试:

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')