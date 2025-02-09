import datetime

# 1
 
datetime.datetime.now() - datetime.timedelta(days=5)

# # 2

print(datetime.datetime.now() - datetime.timedelta(days=1))
print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(days=1))

# 3

datetime.datetime.now().replace(microsecond=0)

# 4

date1 = datetime.datetime(2007, 11, 30, 0, 0, 0)
date2 = datetime.datetime(2007, 11, 7, 0, 0, 0)

diff = date1 - date2

print(diff.total_seconds())
