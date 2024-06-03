import xml.etree.ElementTree as ET
import random

#文件路径
file_path = "selected1km_rl.rou.xml"

# 读取XML文件
tree = ET.parse(file_path)
root = tree.getroot()

# 找到所有id属性为rl的vType标签
rl_vtypes = [vtype for vtype in root.findall('vehicle') if vtype.get('type') == 'rl']

# 计算90%的数量
count_to_replace = int(0.9 * len(rl_vtypes))

# 随机选择90%的rl_vtypes进行替换
vtypes_to_replace = random.sample(rl_vtypes, count_to_replace)

# 替换选中的vType标签的id属性为HDC
for vtype in vtypes_to_replace:
    vtype.set('type', 'HDC')
 
# 保存修改后的XML文件
tree.write("output.xml")


