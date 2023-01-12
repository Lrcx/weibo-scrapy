import random

import requests
from lxml import etree
import pandas as pd
import pickle

import time

ips = [
{'http': '202.109.157.62:9000'},
{'http': '121.13.252.62:41564'},
{'http': '112.14.47.6:52024'},
{'http': '222.74.73.202:42055'},
{'http': '121.13.252.58:41564'},
{'http': '117.114.149.66:55443'},
{'http': '27.42.168.46:55481'},
{'http': '121.13.252.61:41564'},
{'http': '183.236.232.160:8080'},
{'http': '61.216.156.222:60808'},
{'http': '61.216.185.88:60808'},
{'http': '121.13.252.60:41564'},
]
idx = 0

cookie = '_T_WM=23ab75cf567193a72f8ec9b91f2828f7; SCF=AvDY_vBsXjua6tYHvw4_LKT4y5FIUBh2ijOwBKhNrmkymvx2clDg_iHdguZswK3ZzUxkAvnXphqpkRLs64L8790.; SUB=_2A25OukZPDeRhGeBO6FIQ9inJzj6IHXVqRWoHrDV6PUJbktAKLUb5kW1NSg_nqxhYS2E4jItfEaBg911sF8nGcLR8; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF7lcLj6_vblXhZLZBKa_nM5JpX5K-hUgL.Foq7e05pSoMfSKz2dJLoI7UeMJSRdc4L; SSOLoginState=1673410079; ALF=1676002079'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
headers = {'User_Agent': user_agent, 'Cookie': cookie}

filename = '%23女权%23'

df=pd.read_csv(filename+'.csv',header=0)

gender = []
district = []


for data in df.itertuples(index=False):
    user_id = data[2]
    url = 'https://weibo.cn/%s/info' % (user_id)

    #随机产生一个ip
    idx = idx%len(ips)
    resp = requests.get(url, headers=headers , proxies=ips[idx] )
    idx +=1

    # print(resp.content)
    selector = etree.HTML(resp.content)
    # resp.close()
    # 中间可能有认证选项，所以性别可能排在第三位也可能排在第四位
    info_lists = selector.xpath("//div[@class='c']/text()")
    print(info_lists)
    for info in info_lists:
        info = str(info)
        if '性别' in info:
            gender.append(info.split(':')[1])
            break
    for info in info_lists:
        if '地区' in info:
            if len(info.split(':'))==2:
                district.append(info.split(':')[1])

    time.sleep(1)

print(gender)
print(district)


## 持久化
with open(filename+'_gender.txt','wb') as f:
    pickle.dump(gender,f)
with open(filename+'_district.txt','wb') as f:
    pickle.dump(district,f)