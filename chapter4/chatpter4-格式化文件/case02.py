import xml.etree.ElementTree

root = xml.etree.ElementTree.parse('******.xml')
print('利用getiterratory访问')
nodes = root.getiterator()
for node in nodes:
    print('{0}---------{1}'.format(node.tag, node.text))

print('find=============findall')

ele_list1 = root.find('节点名称')
print('ele_list===========type------'+type(ele_list1))
print('{0}---------{1}'.format(ele_list1.tag, ele_list1.text))


ele_list2 = root.findall('节点名称')
for ele in ele_list2:
    print('{0}---------{1}'.format(ele_list2.tag, ele_list2.text))
    for sub in ele.getiterator():
        print('{0}---------{1}'.format(sub.tag, sub.text))