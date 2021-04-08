import os
import sys
import subprocess
import datetime
from time import sleep

t = sys.argv[1] # A record
n = sys.argv[2] # new IP to compare
d = sys.argv[3] # DNS server

cmd = ["nslookup", t, d]

start = datetime.datetime.now()
print("Starting ...", start.strftime("%Y-%m-%d %H:%M:%S"))
while True: 
    #print("checking ...")
    output = subprocess.run(cmd, capture_output=True)
    if (str(output)).count(n) > 0:
        end = datetime.datetime.now()
        print("Done ...", end.strftime("%Y-%m-%d %H:%M:%S"))
        print("Took ", (end-start).total_seconds(), "sec to finish")
        exit()
    sleep(5) 





