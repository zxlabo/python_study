import os
import sys
import re
import psutil
import signal

p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.extend([p])

from work.common import log

if __name__ == '__main__':
    # 先停止所有任务
    pids = []
    for p in psutil.process_iter():
        try:
            found = re.search('.+/pontus/l[0-9]+/__robot.+', p.cmdline()[1])
            if found and p.pid != os.getpid():
                pids.append(p.pid)
        except Exception as e:
            continue
    if len(pids) > 0:
        for pid in pids:
            log.log('found pid [%d] self [%d]' % (pid, os.getpid()))
            if pid != os.getpid() and pid != 0:
                os.kill(pid, signal.SIGKILL)
                log.log('kill pid %d ' % pid)
