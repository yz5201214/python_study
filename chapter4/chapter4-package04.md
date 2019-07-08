# os -操作系统相关 
* 跟操作系统相关，主要是文件操作 案例：chapter4-package04->case01.py
    * 与操作相关的操作，主要包含在三个模块里面
        * os 操作系统目录相相关
        * os.path 系统路径相关操作
        * shutil 高级文件操作，目录树的操作，文件复制，删除，移动
    * 路径
        * 绝对路径 从根目录开始
        * 相对路径 从当前环境开始的一个相对的位置
    * os
        * getcwd()获取当前的工作目录
    * 值部分 主要是为了保证代码的复用性，移植性
        * os.curdir: curreten dir ,当前目录
        * os.pardir: parent dir ,父目录
        * os.sep: 当前系统的路径分隔符
            * windows : "\"
            * linux: "/"
        * os.linesep:当前系统的换行符
            * windos: "/r/n"
            * linux,unix,makos: "/n"
        * os.name: 当前系统名称
            * windos: "nt"
            * linux,unix,makos: "posix"
* os.path 模块，跟路径相相关的模块
    * 详情参考案例:case01.py
* shutile模块，文件操作
    * 详情参考案例:case01.py
    * copy(),move()
* 归档和压缩
    * 归档：把多个文件或者文件夹合并到一个文件当中
    * 压缩：用算法把多个文件或者文件夹无损或者有损的合并到一个文件当中
        * 有损：类似图片清晰度处理
        * 无损：完全原样压缩处理，对文件本质没任何处理
    * zip - 压缩包 案例：case01.py
        * 模块名称叫 zipfile
* random 案例：case02.py
    * 随机数函数
    * 所有的随机模块都是伪随机
    