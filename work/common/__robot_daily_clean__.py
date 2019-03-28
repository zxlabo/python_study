import os
import sys
import re
import psutil
import signal
import datetime
import shutil

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
    try:
        # 迁移日志文件
        os.rename('/root/log/', '/root/log-%s/' % log.today())
    except OSError as e:
        log.log('handle OSError [%s]' % repr(e))
    if not os.path.isdir('/root/log/'):
        os.mkdir('/root/log/')
    try:
        # 删除超过7天的日志
        paths = os.listdir('/root/')
        for path in paths:
            found = re.search('log-[0-9]+-[0-9]+-[0-9]+', path)
            log.log('start check path [%s]' % path)
            if found:
                day = datetime.datetime.strptime(found.group()[4:], '%Y-%m-%d')
                before = log.previous_datetime(6)
                if day <= before:
                    del_path = '/root/%s' % path
                    log.log('remove [%s] execute' % del_path)
                    shutil.rmtree(del_path)
    except OSError as e:
        log.log('handle OSError [%s]' % repr(e))
