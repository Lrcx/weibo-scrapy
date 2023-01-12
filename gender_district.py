import pickle
from pyecharts.charts import Bar
from pyecharts import options as opts

filename = '%23女权%23'

with open(filename+"_gender.txt",'rb') as f:
    gender = pickle.load(f)

with open(filename+"_district.txt", 'rb')  as f:
    district = pickle.load(f)

gender_men = 0
gender_women = 0
for i in gender:
    if i == '男':
        gender_men+=1
    else:
        gender_women+=1

print(gender_men)
print(gender_women)

provinces = ['北京','天津','河北','山西','内蒙','辽宁','吉林','黑龙','上海','江苏','浙江','安徽','福建','江西','山东',
             '河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆','香港','澳门','台湾','其他','海外']

map_data = {i:0 for i in provinces}
for i in district:
    for j in provinces:
        if j in i:
            map_data[j]+=1




print(map_data)
bar = Bar(init_opts=opts.InitOpts(width="1500px"))
bar.add_xaxis(list(map_data.keys()))
bar.add_yaxis("女权", list(map_data.values()))
bar.set_global_opts(title_opts=opts.TitleOpts(title="微博发布省份统计图"))
bar.render()




