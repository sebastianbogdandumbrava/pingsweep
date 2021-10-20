import os
import sys
import thread

ipfile = sys.argv[1]
ipfilefd = open(ipfile, "r")
iplist = []

for line in ipfilefd:
    iplist.append(line.strip())

lock = thread.allocate_lock()
threads = []
numthreadsdone = 0
status = []

def ping(ip):
    global status, numthreadsdone
    response = os.system("timeout 1s ping -c 1 " + ip.strip() + " > /dev/null 2>&1")
    
    lock.acquire()
    if response == 0:
        status.append(ip.strip())
    numthreadsdone += 1
    lock.release()
    return response

for ip in iplist:
    thread.start_new_thread(ping, (ip,))

while numthreadsdone < len(iplist):
   pass

for s in status:
    print(s)

