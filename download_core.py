#the core of DownCtrl is open-source
#params:[url(str),md5(str),path(str)]

import sys
import requests

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400'}

def download(url,md5,path):
    res=requests.get(url,headers=header)
    print(res)
    cont=res.content
    file=open(path,'wb')
    file.write(cont)
    file.close()
    return

if __name__=='__main__':
    download(sys.argv[1],sys.argv[2],sys.argv[3])
