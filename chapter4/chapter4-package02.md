# 异常处理
* 广义上的错误分为错误和异常
* 错误指的是可以认为避免的
    * 指的是人为书写或者操作上的失误，可以修改调整
* 异常是指在语法逻辑正确的前提下，出现的问题
    * 异常基本上是不可避免的，所有程序员都写过BUG，异常
* python里面，异常是一个类，可以处理和使用，类似java里面的异常处理，捕获，处理
* 代码的健壮的重要性
    * python标准异常  有时间就看看  
    异常名称````````````描述  
    * BaseException	所有异常的基类  
    SystemExit	解释器请求退出  
    KeyboardInterrupt	用户中断执行(通常是输入^C)    
    * Exception	常规错误的基类  
    StopIteration	迭代器没有更多的值  
    GeneratorExit	生成器(generator)发生异常来通知退出  
    StandardError	所有的内建标准异常的基类  
    ArithmeticError	所有数值计算错误的基类  
    * FloatingPointError	浮点计算错误  
    * OverflowError	数值运算超出最大限制  
    * ZeroDivisionError	除(或取模)零 (所有数据类型)  
    * AssertionError	断言语句失败       
    * AttributeError	对象没有这个属性  
    EOFError	没有内建输入,到达EOF 标记  
    EnvironmentError	操作系统错误的基类  
    IOError	输入/输出操作失败  
    OSError	操作系统错误  
    WindowsError	系统调用失败  
    * ImportError	导入模块/对象失败  
    LookupError	无效数据查询的基类  
    * IndexError	序列中没有此索引(index)  
    * KeyError	映射中没有这个键  
    * MemoryError	内存溢出错误(对于Python 解释器不是致命的)  
    * NameError	未声明/初始化对象 (没有属性)  
    * UnboundLocalError	访问未初始化的本地变量  
    ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象  
    * RuntimeError	一般的运行时错误  
    * NotImplementedError	尚未实现的方法  
    * SyntaxError	Python 语法错误  
    * IndentationError	缩进错误  
    * TabError	Tab 和空格混用  
    SystemError	一般的解释器系统错误  
    * TypeError	对类型无效的操作  
    * ValueError	传入无效的参数  
    UnicodeError	Unicode 相关的错误  
    UnicodeDecodeError	Unicode 解码时的错误  
    UnicodeEncodeError	Unicode 编码时错误  
    UnicodeTranslateError	Unicode 转换时错误  
    Warning	警告的基类  
    DeprecationWarning	关于被弃用的特征的警告  
    FutureWarning	关于构造将来语义会有改变的警告  
    OverflowWarning	旧的关于自动提升为长整型(long)的警告  
    PendingDeprecationWarning	关于特性将会被废弃的警告  
    RuntimeWarning	可疑的运行时行为(runtime behavior)的警告  
    SyntaxWarning	可疑的语法的警告  
    UserWarning	用户代码生成的警告

* 没有程序员能够保证程序永远正确运行
* 但是，必须保证程序在最坏的情况下出现的问题被妥善处理
* python最基本的异常处理模块全部语法为：   与java基本一致  案例：exceptCase->exceptCase01.py  
    try:  
        &emsp;尝试实现某个操作    
    except 异常类型1  
        &emsp;解决方案1：  尝试解决异常  
    except 异常类型2  
        &emsp;解决方案2：  尝试解决异常  
    except (异常类型1,异常类型2....)  
        &emsp;解决方案：多种错误统一进行解决  
    else:  
        &emsp;如果没有异常，执行这里  
    finally:  
        &emsp;完成后执行，无论有没有异常
* 如果是多种error的情况，越具体的错误，请放越前面，在异常类继承关系中，越是子类，越要靠前捕获，父类往往靠后处理
* 异常捕获后，如果没有exit()停止处理，那么代码将继续往下执行
* 程序员手动触发异常
    * raise 关键字来触发异常
* 自定义异常
    * 自定义异常必须是系统异常的子类
    * raise 推荐使用自定义异常
        * 自定义异常的异常代码可自行处理
        * 自定义异常后的问题提示可以自行处理
        * 自定义异常位置
    * 主要是为了方便快速定位异常位置
    