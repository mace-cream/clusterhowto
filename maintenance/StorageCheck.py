import os
import time
import threading

path = '/home/zhiyuan/'
limit = 1*1024*1024
log_file = '/home/zhiyuan/du.log'

_f = open(log_file,'a')
_f.write("[LOG]"+' '+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))+' Program start.\n')
threads = []

def check(target):
    size = os.popen('du -s ' + path + target).readlines()[0].split('\t')[0]
    if float(size) > limit:
        _f.write("[LOG]"+' '+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))+' Exceed Limit: '+target+' '+str(size)+'\n')

for target in os.listdir(path):
    threads.append(threading.Thread(target = check, args=(target,)))
    threads[-1].start()

for x in threads:
    x.join()

_f.write("[LOG]"+' '+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))+' Program stop.\n')
_f.close()