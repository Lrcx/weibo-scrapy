import pickle
from pyecharts.charts import Bar
from pyecharts import options as opts

filename_nvquan = '%23女权%23'
filename_tianyuan = '%23田园女权%23'
filename_nanquan = '%23男权%23'

with open(filename_nvquan+"_district.txt", 'rb')  as f:
    district_nvquan = pickle.load(f)
with open(filename_nanquan+"_district.txt", 'rb')  as f:
    district_nanquan = pickle.load(f)
with open(filename_tianyuan+"_district.txt", 'rb')  as f:
    district_tianyuan = pickle.load(f)




provinces = ['北京','天津','河北','山西','内蒙','辽宁','吉林','黑龙','上海','江苏','浙江','安徽','福建','江西','山东',
             '河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆','香港','澳门','台湾','其他','海外']

map_data_nvquan = {i:0 for i in provinces}
map_data_nanquan = {i:0 for i in provinces}
map_data_tianyuan = {i:0 for i in provinces}
for i in district_nvquan:
    for j in provinces:
        if j in i:
            map_data_nvquan[j]+=1
for i in district_nanquan:
    for j in provinces:
        if j in i:
            map_data_nanquan[j]+=1
for i in district_tianyuan:
    for j in provinces:
        if j in i:
            map_data_tianyuan[j]+=1



bar = Bar(init_opts=opts.InitOpts(width="1500px"))
bar.add_xaxis(list(map_data_nvquan.keys()))
bar.add_yaxis("女权", list(map_data_nvquan.values()))
bar.add_yaxis("田园女权", list(map_data_tianyuan.values()))
bar.add_yaxis("男权", list(map_data_nanquan.values()))
bar.set_global_opts(title_opts=opts.TitleOpts(title="微博发布省份统计图"))
bar.render()




