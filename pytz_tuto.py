# How to manage clients with different local time zones...

from datetime import datetime

import pytz
from pytz import utc

print("1--------------------------")
now = datetime.now()

# Note that we didn't yet associate a timezone to now datetime
print(now)


# Let's create a timezone we would like to work in
# Here we create a US/Mountain time zone, it knows things about if to run daylight savings time,
# how many time offset from GMT,
mtn = pytz.timezone('US/Mountain')
print("2--------------------------")
print(type(mtn))


print("3--------------------------")
print(now.astimezone(mtn))


# The problem is that we didn't tell what timezone "now" is
# We need to localize it first
print("4--------------------------")
utc_now = utc.localize(now)
print(utc_now)

print("5--------------------------")
print(ut)
