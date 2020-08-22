# -- coding: utf-8 --
import os
import subprocess
import time

# !!!需要下载安装windump并将其添加到环境变量
# 改用其他命令行抓包工具效果相同，相应修改命令即可

pcap_dir=r'E:/datatest'

def dumppcap(appname,operation):
    time.sleep(1)
    print('To 【start】 the capture, please key down y...')
    while 1:
        s = input()
        if s == 'y':
            break
        else:
            print('Tap y to make sure')

    timestamp = time.time()
    pcap_appdir = pcap_dir + '/{0}'.format(appname)
    if not os.path.exists(pcap_appdir):
        os.makedirs(pcap_appdir)
    pcap_filepath = pcap_appdir + '/ad_{0}_{1}.pcapng'.format(operation, timestamp)
    cmd_input = 'windump -n -i 4 -s 0 -w {0}'.format(pcap_filepath)  # 此处需要根据PC网卡情况对命令进行修改
    child = subprocess.Popen(cmd_input)
    time.sleep(2)
    print('Start to capture!')
    time.sleep(1)

    print('To 【end】 the capture, please key down y...')
    while 1:
        s = input()
        if s == 'y':
            print('Capture finished')
            break
        else:
            print('Tap y to make sure')
    time.sleep(3)

    child.kill()


if __name__=='__main__':
    pcap_num=15 # 预期采集的pcap数目
    appname='facebook'  # 预期采集的应用名
    operation='sendmsg'  # 预期采集的行为名
    print('Prepared to start...')
    time.sleep(3)
    print('**************************')
    for i in range(pcap_num):
        dumppcap(appname,operation)
        print('----------------------------')
time.sleep(2)
print('==========================')
print('Finished.')
