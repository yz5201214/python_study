import  xml.dom.minidom
from xml.dom.minidom import parse

# 读取文件
DomTree = xml.dom.minidom.parse("文件路径")
# 得到文档对象
doc = DomTree.documentElement
# 遍历文档中所有的子元素
for ele in doc.childNodes:
    if ele.nodeName == '指定元素标签':
        print('第一个子元素标签名'.format(ele.nodeName))
        # 得到子元素下面其他所有的子元素
        childs = ele.childNodes
        for child in childs:
            # 得到节点属性名称
            print(child.nodeName)
            # 得到节点属性值
            print(child.childNodes[0].data)
