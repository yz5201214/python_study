#多线程
* https://www.cnblogs.com/jokerbj/p/7460260.html
* http://www.dabeaz.com/python/UnderstandingGIL.pdf 全英文
# 多线程 VS 多进程
* 程序：一堆代码以文本形式存入一个文档
* 进程：程序运行的一个状态
    * 包含地址控件，内存，缓存，数据栈等
    * 每个进程由自己完全独立的运行环境，多进程共享数据是一个问题。
* 线程
    * 一个进程的独立运行片段，一个进程可以由多个线程
    * 轻量化的进程
    * 一个进程的多个线程间共享数据和上下文运行环境
    * 共享互斥问题
* 全局解释器锁(GIL)
    * Ptyhon代码的执行是有python虚拟机进行控制的
    * 在主循环中，只能由一个控制线程在执行
* Pythone包
    * _thread 参考案例：case01.py
    * thread：有问题，不好用，python3改成了_thread
    * threading：通用的线程包
    * threading的使用 参考案例：case02.py
        * 直接利用threading.Thread生成Tread实例
            1.t = threading.Thread(target=方法,args=(参数1,参数2,))
                t.start()：启动线程
                t.join()：等待多线程执行完成
        * python多线程，没有父子结构，都是平行结构
        * 守护线程 - daemon 案例：case02.py
            * 如果在程序中将子线程设置成守护线程，则子线程在主线程结束的时候，自动退出
            * 一般认为，守护线程不重要或者不允许离开主线程独立运行
            * 守护线程案例能否有效跟环境有关
            * 如果不指定线程是否是守护线程，默认非守护线程，线程互相独立
        * 线程常用属性 案例：case02.py
            * threading.currentThread：返回当前线程变量
            * threading.enumerate：返回一个包含正在运行的线程的list，正在运行的线程指的是线程启动后，结束前的状态
            * threading.activeCount：返回正在运行的线程数量，效果跟len(threading.enumerate)相同
            * threading.setName：给线程设置名称
            * threading.getName：得到线程名称
    * 直接继承自threading.Thread
        * 直接继承Thread
        * 重写run函数
        * 类实例可以直接运行
        * 案例case03.py
        * 案例case04.py 正常项目写法
            
            