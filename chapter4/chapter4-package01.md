# 1. 模块
* 建议所有的模块入口，统一使用mian方法作为入口，python的mian跟java的mian实际效果一致
* 一个模块就是一个包含python代码的文件，后缀名是.py就可以，模块就是一个python文件
* 为什么我们用模块 有点类似java的架包概念
    * 程序太大，编写维护非常不方便，需要拆分
    * 模块可以增加代码重复利用的方式
    * 当作命名空间使用，避免命名冲突
* 如果定义模块
    * 模块就是一个普通文件，所以任何代码都可以直接书写
    * 不过根据模块的规范，最好的模块中编写一下内容
        * 函数（实现单一功能），有点类似Mixin写法，单一功能函数
        * 类（相似功能的组合，或者类似相同业务模块）
        * 测试代码（模块内必须包含模块测试代码）
* 如果使用模块 案例：package01.py ,package02.py
    * 模块直接导入
        * 假如模块名称直接以数字开头，需要借助importlib帮助
    * 语法：案例package02.py
    * import 模块 as 别名    类似sql语句
    * from module_name import func_name,class_name 
        * 从某个模块，导入指定方法或者类 案例：package03.py
        * 使用导入模块的内容时，不需要使用前缀，直接调用即可
    * from module_name import *  案例：package04.py
        * 效果等同于import 模块
        * 优点：不需要使用前缀调用，直接使用
        * if __name__ == "__main__"的使用
* 2.模块的搜索路径和存储 package05.py
    * 什么是模块的搜索路径
        * 加载模块的时候，系统会在哪些地方寻找该模块
    * 系统默认的模块搜索路径
        import sys
        print(sys.path)可以查看所有的模块路径，list类型，可以遍历输出
    * 添加搜索路径
        * sys.path.append(dir)
    * 模块加载顺序
        * 搜索内存中已经加载号的模块
        * 搜索python的内置模块
        * 搜索sys.path的路径
# 包
* 包是一种组织管理你代码的方式，包里面存的是模块
* 用于将模块包含在一起的文件夹就是包
* 自定义包的结构：

    |- - - 包  
    |- - - |- - - __init__.py 包的标志文件  
    |- - - |- - -  模块1  
    |- - - |- - -  模块2  
    |- - - |- - -  子包(子文件夹)  
    |- - - |- - - |- - -  __init__.py 包的标志文件  
    |- - - |- - - |- - -  子包模块1  
    |- - - |- - - |- - -  子包模块2  
    
* 包的导入操作
    * import package_name
        * 直接导入一个包，可以使用__init__.py中的内容
        * 使用方法是：  
            package_name.func_name  
            package_name.class_name.func_name()  
        * 此种方式的访问内容是： 案例：package05.py
        * 包的导入也可以使用别名
         * 注意包的导入，会针对包内的__init__.py内容的导入和调用
    * import package.module
        * 导入指定包的指定模块 案例：subPackage01.py,package05.py
        * 使用方法  
              package.module.func_name  
              package.module.class.fun()
              package.module.class.var
    * from .....import 导入
        * from package import module1, module2, module3
            * 这种方法导入，不会执行__init__的内容，自动过滤
        * from package  import * 
            * 导入当前包__init__.py 文件中所有的函数和类，不包括其他模块
            * 使用方法    
                func_name()  
                class_name.func_name()  
                class_name.var  
            * 包中__all__ 的用法 package06.py
            * 在使用from package import * 的时候，* 可以导入的内容
            * 文件__init__.py 中如果文件为空，护着没有__all__，那么只可以把__init__中的内容全部导入
            * `__init__.py` 如果设置了`__all__`的值，那么按则按照`__all__`指定的子包或者模块进行导入，并不会导入`__init__`内全部内容
            * 案例：package.subpackage02中的`__init__`
    * from package.module import * 
        * 导入包中指定模块的所有内容
        * 使用方法  
            func_name()  
            class_name.func_name()  
            class_name.var    
* 在开发环境中经常会使用其他模块，可以再当前包中直接导入其他模块中的内容
    * import 完整的包或者模块的路径，(存放路径)
* 命名空间
    * 用于区分不同位置不同功能但是相同名称的函数或者变量的一个特定前缀
    * 作用是防止命名冲突  
        setName()  
        Student.setName()  
        Dog.setName()  
    
