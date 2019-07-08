import json

jsonStr = {'name':'yuanwai','age':18,'mobile':'1231231321','boolean':'true'}

def test01():
    print(type(jsonStr))
    python_json = json.dumps(jsonStr)
    print(type(python_json))
    print('json对象{0}'.format(python_json))
    # dict Python字典
    python_dict = json.loads(python_json)
    for i in python_dict:
        print(i,'--------------------------',python_dict[i])
    print(type(python_dict))
    print('11111111json对象{0}'.format(python_dict))

def test02():
    # 写json文件，如果没有，则自动创建
    with open('t.json','w') as f:
        json.dump(jsonStr,f)
    #读json文件
    with open('t.json','r') as f:
        d = json.load(f)
        print(d)

if __name__ == '__main__':
    test01()