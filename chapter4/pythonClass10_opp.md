# makdown语法的熟悉~~~


# OOP - python的面向对象
- python也是一门面向对象的语言
- 面向对象编程
    - 基础
    - 公有，私有
    - 继承
    - 组合，Mixin
- 各种魔法函数
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数
    
# 1 面向对象概述 (ObjectOriented,00)
- OOP思想 借助java编程思想里面的套路，万事万物皆对象，对象有属性，有动作
    - 接触到任意一个任务，首先想到的是任务这个世界的构成，是由模型构成的
    - OO 面向对象
    - OOA 面向对象的分析
    - OOD 面向对象的设计
    - OOI 面向对象的实现
    - OOP 面向对象的编程
    - 顺序，先分析，然后设计，达到实现，最后编程
    
- 类和对象的概念
    - 类：抽象名称，代表一个集合，共性的事物。表示有一种或者多种共性的个体集合
    - 对象：具体的事物，单个个体，类由多个对象组成
    - 类与对象的关系
        - 一个具像，代表一类事物的某一个个体
        - 一个是抽象，代表的是多个具象
    - 类中的内容，应该具有两个内容
        - 表明事物的特征，叫做属性(变量)
        - 表明事物的功能叫做动作，编程里面叫方法(函数)
# 2 类的基本实现
- 类的命名
    - 命名规范，常规使用大驼峰
    - 命名尽量避免关键字
- 声明一个类
    - 必须使用class关键字
    - 类由属性和方法构成，其他不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有值，允许使用None，空值
    - 案例 case/oopCase1.py
- 实例化类
    - 实例化，参考案例
    - 访问对象成员，参考案例 
    - 检查对象成员，可以通过默认内置变量检查类和对象的所有成员  
        -obj.__dict__，注意双下划线
        -class_name.__dict__ 
    
# 3 anaconda基本使用
- anaconda主要是一个虚拟环境的管理器
- 还是一个安装包管理员
- conda list：显示anaconda安装的包
- conda env list：显示anaconda的虚拟环境列表
- conda create -n 名称 python=3.6 创建一个版本为3.6的虚拟环境，名称为XXX
    
# 4 类的成员对象分析 案例：oopCase2.py
- 类和对象都可以存储成员，成员可以归类所有，也可以归对象所有
- 类存储成员时，使用的是与类关联的一个对象
- 独享存储成员时使用的是与类关联的衣蛾对象
    - 类只能存在一个申明，但是可以有多个实例
- 对象访问一个成员时，如果对象中有该成员，尝试访问类中同名成员。如果对象中有
- 创建对象的时候，类中的成员不会放入对象当中，而是得到一个空对象，没有成员
- 通过对象对类中成员的重新赋值或者通过对象添加成员时，对应成员会保存在对象中，而不会修改该类成员

# 5 关于类中的 self
- 可以将self理解成Java中的this，或者JavaScript的this，可以这样理解
- self 在对象的方法中表示对象本身，如果通过对象调用一个方法，那么该对象会自动传入到当前方法的第一个参数里面
- self 并不是关键字，只是一个普通对象命名，可以根据自身喜好调整
- 方法有self形参的方法称为非绑定类的方法，可以通过对象访问，没有self的是绑定类的方法，只能通过类访问
- 使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员

# 6 面向对象的三大特征 
- 封装
- 继承
- 多态
    - 封装  案例：oopCase3.py
        - 封装就是对对象的成员进行访问限制
        - 封装的三个级别 python中public,private,protected不是关键字，python更多的是使用类这种思路
            - public 公开
            - protected 受保护的
            - private 私有
        - 级别判断条件
            - 对象内部
            - 对象外部
            - 子类中
        - 私有 
            - python的私有不是真的私有,是一种伪私有，是一种成为name mangeling的改名策略，意思就是：实际上参数还在，只是改了个你不知道的名称，可以强行访问，不建议
            - 私有成员是最高级别的封装，只能在当前类或者对象中访问
            - 在成员前面添加两个下划线即可 即：__name = "xxx"
        - 受保护的封装 protected
            - 受保护的封装是将对象成员进行一定级别的封装，然后，在类中或者自雷中都可以进行访问，但是外部不可以
            - 封装方法：在成员名称前添加一个'_'下划线即可
        - 公开的，共有的，public
            - 公共的封装实际对成员没有任何操作，任何地方都可以访问
    - 继承  案例：coopCase4.py java中常见的extentds
        - 继承就是一个类可以获得另外一个类中的成员属性和成员方法
        - 继承的作用就是减少重复，冗余的代码量，增加代码复用程序，同时可以设置类与类直接的关系
        - 继承与被继承的概念：
            - 被继承的类叫父类，也叫基类，也叫超类，根据自身喜好
            - 用于继承的类，叫子类，也叫派生类
            - 继承与被继承一定存在一个 is-a 关系
        - 继承的特征
            - 所有类都继承自Object类，即所有的类都是Object类的子类
            - 子类一旦继承父类，则可以使用父类中除私有成员外的所有内容
            - 子类继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用
            - 子类中可以定义独有的成员属性和方法
            - 子类中的成员如果和父类成员命名相同，优先使用子类自由成员
            - 子类如果想扩充父类的方法，可以在定义新方法的同时，访问父类成员来进行代码重用
                可以使用[父类名.父类成员] 的格式来调用父类成员，也可以使用[super().]成员名来调用
        - 继承函数的变量查找顺序问题
            - 任何情况都是与优先查找自己的变量
            - 如果没有则查找父类
            - 构造函数如果本类中没有定义，则自动查找调用父类的构造函数
            - 如果本类有定义，则不继续向上查找
        - 构造函数
            - 是一种特殊的函数，在类进行实例化之前进行调用
            - 构造函数在初始化的时候，如果存在继承关系，会一直往上查找，都定义的情况下，优先调用在子类
            - 构造函数在实例化的时候，需要传入对应的类型参数，self表示本身，可以不传，其他参数在实例化的时候，需要传入
            - 如果子类没有自定义构造函数，但是父类有多参数的构造函数，在子类初始化的时候，需要传入参数，因为调用的是父类构造函数
        - super 
            - super 并不是关键字，而是一个类
            - super 的作用是获取MRO(MerthodResolustionOrder)列表中的第一个类
                类名称.__mro__ 获取该类的所有父类
            - super 于父类没有任何实质性的关系，但是通过super可以调用到父类
            - super 常规使用的两个方法，参见：oopCase4.py 调用父类构造函数
        - 单继承和多继承 oopCase5.py
            - 单继承：每个类只能继承一个类
            - 多继承：每个类允许继承多个类，但是多个类继承会带来很多麻烦，java不允许，但是python允许
            - 单继承和多继承的优缺点
                - 单继承：
                    - 优点：传承有序，逻辑清楚，语法简单，隐患少
                    - 缺点：功能不能无限扩展，只能在当前唯一的继承链中扩展
                - 多继承：
                    - 优点：类的功能扩展方便
                    - 缺点：继承关系混乱
            - 菱形继承/钻石继承问题
                - 多个子类继承自同一个父类，这些子类又被同一个类继承，于是继承关系图形成一个菱形谱，理解会比较混乱
                - [MRO](https://www.cnblogs.com/whatisfantasy/p/6046991.html)
                - 关于多继承的MRO
                    - MRO就是多继承中，用于保存继承顺序的一个列表
                    - Python本身采用C3算法来计算继承的菱形继承进行计算的结果
                    - MPO列表的计算原则：
                        - 子类永远在父类前面
                        - 如果多个父类，则根据继承语法中括号内的父类顺序存放
                        - 如果多个类继承类同一个父类，孙子类中只会选取继承语法括号中的第一个父类的父类
    - 多态 oopCase6.py
        - 多态就是同一个对象在不同的情况下有不同的状态出现
        - 多态不是语法，是一种设计思想
        - 多态性：一种调用方式，不同的执行效果
        - 多态：同一事物的多种心态，动物分为人类，狗，猪等等
        - [多态和多态性](https://www.cnblogs.com/luchuangao/p/6739557.html)
        
        - Mixin设计模式
            - 主要采用多继承方式对类的功能进行扩展
            - [Mixin概念](https://www.zhihu.com/question/20778853)
            - [Mixin模式](https://www.cnblogs.com/xybaby/p/6484262.html)
            - 类似于：物理变化，化学变化的概念。Mixin模式是物理变化
                超人：本身应该是人，他能飞，能游泳，只是一项技能，而不是继承了鱼或者鸟的血统
        - 我们使用多继承的语法来实现Mixin
        - 使用Mixin来实现多继承的时候，需要特别注意
            - 首先他必须表示某一个单一功能，而不是某个物品
            - 指着必须单一，如果有多个功能，则写多个Mixin
            - Mixin不能依赖于子类的实现
            - 子类即使没有继承这个Mixin类，也能照样运行，只是缺少了某个功能
        - Mixin说明：实际就是代码的多继承，只是遵循了Mixin书写，使用规则。Mixin类类似于java里面的工具类
        - 优点：
            - 使用Mixin可以在不对类进行任何修改的情况下，扩充功能
            - 可以方便的组织和维护不同功能组件的划分
            - 可以根据需要任意调整功能类组合
            - 可以避免创建很多新的类，导致类的继承关系混乱
    - 类相关函数 有点像JavaScript
        - issubclass：检测一个类是否是另一个类的子类
        - isinstance：检测一个对象是否是一个类的实例
        - hasattr：检测一个对象是否由xxx成员构成
        - getattr：获取一个对象成员
        - setattr：设置一个对象成员
        - delattr：删除一个对象成员
        - dir：获取对象的成员列表
 # 7 oopCase 终章 oopCase7.py oopCase10.py
* 类的成员描述符(属性)
    * 类的成员描述符是为了在类中对类的成员属性进行相关操作的而创建的一种方式
        * get： 获取属性的操作
        * set： 修改或者添加属性操作
        * delete：删除属性的操作
    * 如果想使用类的成员描述符，大概有三种方法
        * 使用类实现描述器
        * 使用属性修饰符
        * 使用property函数
            * property函数很简单
                * property(fget, fset ,fdel, doc)
    * 无论哪种修饰符都是为了对成员属性进行相应的操作
        * 类的方式：适合多个类中的多个属性共用同一个描述符
        * property：适合当前类中使用，可以控制一个类中的多个属性
        * 属性修饰符：使用与当前类中使用，控制一个类中的一个属性
* 类的内置属性
    * __dict__：以字典的方式显示类的成员组成
    * __doc__：获取类的文档信息，即注释信息
    * __name_：获取类的名称，如果在模块中使用，获取模块的名称
    * __bases__：获取某个类的所有父类，以元祖的方式显示
    
* 类的常用魔术方法 python的牛逼，很大部分在于魔术方法 案例：oopCase8.py 
    * 魔术方法就是不需要人为的调用的方法，基本是在特定的时刻自动触发
    * 魔术方法的统一特征：
        * 方法名被前后各两个下划线包裹
        * 常用的类操作函数：
            * __init__：构造函数
            * __new__：对象实例化的方法。类对象实例化的真实第一个调用的方法。此魔术方法比较特殊，一般不需要使用
            * __call__：对象当函数使用的时候触发
            * __str__：当对象被强转字符串使用的时候，被调用
            * __repr__：返回字符串，与__str__一样，但是python推荐__str__，具体区别需要百度
        * 描述符相关
            * __set__:
            * __get__:
            * __delete__:
        * 属性操作相关
            * __getattr__：访问一个不存在的属性时触发
            * __setattr__：对成员属性进行设置的时候触发
                * 参数：
                    * self：用来获取当前对象
                    * 被设置的属性名称，以字符串形式出现
                    * 需要对属性名称设置的值
                * 作用：进行属性设置的时候进行验证或者修改
                * 注意：在该方法中不能对属性直接进行赋值操作，否则死循环，具体参考案例：oopCase8.py
        * 运算分类相关魔术方法，python提供很多魔术方法，这里只介绍了常用的，其他的可以自行学习
            * __gt__：进行大于判断的时候出发的函数 案例：oopCase8.py
                * 参数：
                    * self
                    * 第二个参数是第二个对象
                    * 返回值可以自行定义，定义成任何内容，推荐判断大小返回boolean


# 8 类和对象的三种方法 参考案例：oopCase9.py
* 实例方法 类似java的普通方法
    * 需要实例化对象才能使用的方法，使用过程中可能需要截止对象的其他方法完成
* 静态方法 类似java的static
    * @staticmethod 声明
    * 不需要实例化，通过类直接访问
* 类方法
    * @classmethod 声明
    * 不需要实例化
    
# 9 抽象类 (基本知识终章) oopCase11.py
* 抽象方法：没有具体实现内容的方法称为抽象方法
* 抽象方法的主要意义是规范了子类的行为和接口
* 抽象类的使用需要借助abc模块 --abc模块后续介绍  import abc
* 抽象类：包含抽象方法的类叫抽象类，通常称为ABC类  与java的抽象类类似，本身不执行任何操作，由继承的子类实现具体操作
* 抽象类的使用
    * 抽象类可以包含抽象方法，也可以包含具体的方法
    * 抽象类中可以有方法也可以有属性
    * 抽象类不允许直接实例化，因为抽象方法没有具体实现，所以不允许实例化
    * 必须继承才可以使用，且继承的子类必须实现所有的父类的抽象方法，与java基本一致
    * 假定子类没有实现所有继承的抽象方法，则子类也不能实例化
    * 抽象类的主要作用是设定类的标准，便于开发的时候具有统一的规范
    
# 11 自定义类 oopCase11.py
* 类其实是一个类定义和各种方法的自由组合
* 函数名称是可以当做变量来使用的 python才有
* 可以定义类和函数，然后自己通过类直接赋值
* 或者借助type实现
* 利用元类实现 - MetaClass
    * 元类说明：
        * 元类也是类
        * 元类是用来创造别的类 案例:oopCase11.py