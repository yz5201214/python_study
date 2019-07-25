# 验证码问题
* 验证码从以往的登录或者搜索验证，慢慢往反爬虫方面转移
* 分类
    * 简单图片
    * 极验
        * 极验官网：http://www.geetest.com/
    * 12306官网：多图片选择验证
    * 电话语音验证：实际就是电话语音验证码
    * google验证：随机书籍等文字内容，需要手动输入
    * 验证码的破解：
        * 通用方法：
            * 下载网页和验证码，然后进行手动输入
            * 实际上还是需要人工操作。
        * 简单图片    
            * 使用图像识别软件或者文字识别软件进行识别
            * 也可以使用第三方图像验证码破解接口
                * 类似：www.chaojiying.com 超级鹰<很出名啊>
        * 极验
            * 破解比较麻烦
            * 可以模拟鼠标移动等操作
            * 极验的验证模式一直在优化，进化。毕竟背后是一家公司，有专业的反爬虫团队
        * 12306官网多图片选择验证
            * 太难，最好手动识别
        * 电话语音验证
            * 利用语音识别，但是会存在一定的误差。技术的进步误差越来越小
        * goole验证
            * 目前已经用的比较少
    * 简单案例：spider-authCode-case12.py
    * Tesseract 简单图片，文字识别模块
        * 机器视觉领域的基础软件
        * OCR技术：OpticalChracterRecongnition，光学文字识别
        * Tesseract：一个OCR库，google赞助
            * 安装教程：https://blog.csdn.net/showgea/article/details/82656515
                * windows：需要下载https://digi.bib.uni-mannheim.de/tesseract/需要的版本
                * 其他环境安装自行百度
        * 安装完成后，Python还需要pytesseract
            
    