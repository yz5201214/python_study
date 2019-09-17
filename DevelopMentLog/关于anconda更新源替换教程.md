# 替换源命令操作
* 问题：执行下面操作升级conda时，下载的速度很慢

conda update conda

解决方案：更换anaconda源，使用清华的源

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/

conda config --set show_channel_urls yes

再次执行升级操作，速度飞起！
