# -- coding: utf-8 --
import subprocess
import os

def filters(inputpath,outputpath):
    cmd='tshark -r '+inputpath+" -2 -R ip.addr==124.156.162.218 -w "+outputpath
    # tinput="tshark -r "+ipath+" -2 -R \"tcp.stream eq "+str(nums)+"\" -w "+opath
    child=subprocess.Popen(cmd)
    subprocess.Popen.wait(child)
    child.kill()


def NewFileName(file):  # 获取新文件名
    name=file.split('.')
    newfilename=name[0]+'_filtered'+'.pcapng'
    return newfilename


inputpath=r'E:\2020fall_appsdata\youtube'
outputpath=r'E:\2020fall_appsdata_filter\youtube'
files=os.listdir(inputpath)
for file in files:
    inputfilepath=inputpath+'\\'+file
    outputfilepath=outputpath+'\\'+NewFileName(file)
    filters(inputfilepath,outputfilepath)
    print('Finish {0}'.format(file))

