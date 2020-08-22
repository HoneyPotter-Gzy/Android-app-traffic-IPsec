# -- coding: utf-8 --
import subprocess
import os
import time


pcap_filepath=r'E:\datatest\facebook'  # 原始pcap所在文件夹
ip='108.160.141.197'  # 填入IPSec隧道所连接的远程vps地址，用于后续按ip进行流量过滤，去除PC端的杂包
os.chdir(pcap_filepath)
files=os.listdir(pcap_filepath)
nums=len(files)
finish_nums=0

for file in files:
    newfile=file.split('.')[0]+'.'+file.split('.')[1]+'_.pcapng'
    cmd_input='tshark -r {0} -2 -R "ip.addr=={2}" -w {1}'.format(file,newfile,ip)
    # print(cmd_input)
    child=subprocess.Popen(cmd_input)
    subprocess.Popen.wait(child)
    time.sleep(1)
    child.kill()
    finish_nums+=1
    percent=str(round((finish_nums/nums)*100, 2))+'%'
    print('Finished {0},【{1}】 accomplished...'.format(newfile,percent))
    print('----------------------')

print('========================')
print('All files finished.')

