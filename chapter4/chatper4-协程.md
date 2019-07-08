#协程
* 参考资料
    * http://python.jobbole.com/86481/
    * http://python.jobbole.com/87310/
    * http://segmentfault.com/a/119000000978168
#迭代器
* 案例：case01.py
* 可迭代(Iterable)：可直接组用于for循环的变量
* 迭代器(Iterator)：不但可以作用于for循环，还可以被next调用
    * list是典型的可迭代对象，但是不是迭代器
    * isinstance案例 判断某个变量是否是一个实例，是否可以迭代
    * iterable 和 Iterator 可以转换
        * 通过iter
# 生成器
* 案例case02.py
* generator：一遍循环一遍计算下一个元素的机制/算法
* 需要满足于三个条件：
    * 每次调用都生成处for循环需要的下一个元素或者对象
    * 如果达到最后一个，爆出StopIteration异常
    * 可以被next函数调用
    * 如何生成一个生成器，看案例
        * 直接使用
        * 如果函数中包含yield，则这个函数就叫生成器
        * next调用函数，遇到yield返回
# 协程
* 案例：case03.py
* 历史
    * 3.4引入协程，用yield实现
    * 3.5引入携程语法
    * 实现的协程比较好的包有asyncio，tornado，gevent
* 定义
    * 协程是为了非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停或开始执行程序。
    * 从技术角度讲，协程就是一个你可以暂停执行的函数，或者可以理解成生成器
* 协程的实现
    * yield 返回
    * send 调用
* 协程的4个状态
    * inspect.getgeneratorstate(...)函数确定，该函数会返回下述字符串中的一个：
        * GEN_CREATED：等待开始执行
        * GEN_RUNNING：解释器正在执行
        * GEN_SUSPENED: 在yield表达式处在暂停
        * GEN_CLOSED：执行结束
        * next预激(prime)
        * 案例case03.py
* 协程的终止
    * 协程中为处理的异常会向上冒泡，传给next函数或者send方法的调用方法(即触发协程的对象)
    * 终止协程的一种方法：发从某个哨兵符号，让协程退出，内置的None和Ellipsis灯亮警察用作哨兵符号
* yield from 
    * 案例case04.py
    * 调用协程为了得到返回值，协程必须正常终止
    * 生成器正常终止会发出StopIteration异常，异常对象的value属性保存返回值
    * yield from 从内部捕获StopIteration异常
    * 委派生成器
        * 可以理解成中间库的意义
        * 包含yield from表达式的生成器函数
        * 委派生成器在yield from表达式出现暂停，调用发可以直接把数据发给子生成器
        * 子生成器再把产出的值发送给调用方
        * 子生成器在最后，解释器会抛出StopIteration异常，并且把返回值附加到异常对象上
        - 案例 case04.py
* 优势：
    协程对资源的消耗基本可以忽略不计，相对复杂的多线程，协程可以更好的利用资源