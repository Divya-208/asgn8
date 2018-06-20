
import time
print(time.gmtime(0))

#2.wapto get formatted time
import time
print(time.asctime(time.localtime(time.time())))




# 3.extract month from time
from datetime import datetime
d=datetime.now()
print(d
print(d.strftime("%B")))

#4.extract day from the time
from datetime import datetime
d=datetime.now()
print(d)
print(d.strftime("%A"))

#5.extractdate(ex:11in 11/01/2021) from the time
import time


print(time.localtime(time.time()))
print(time.asctime(time.localtime()))
l=list(time.localtime())
print(l)s
print(l[2])


#6. import time
print(time.localtimeint(())

#7.fact.of no.
import math
print(math.factorial(10))

#8.find gcd of no.
import math
print(math.gcd(30,50))


#9.use os package
import os
print(os.getcwd())
print(os.name)
print(os.listdir)
print(os.environ)
