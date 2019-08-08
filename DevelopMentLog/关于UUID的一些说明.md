# uuid
* 食用方法
    * 直接import uuid即可
    * 四个方法 ，注意没有2
        * uuid1()：根据时间戳+mac地址生成，容易暴露mac地址
            * uuid.uuid1()
        * uuid3()：里面的namespace和具体的字符串都是我们指定的，然后呢···应该是通过MD5生成的，这个我们也很少用到，莫名其妙的感觉。
            * uuid.uuid3(uuid.NAMESPACE_DNS, 'yuanlin')
        * uuid4()：这是基于随机数的uuid，既然是随机就有可能真的遇到相同的，但这就像中奖似的，几率超小，因为是随机而且使用还方便，所以使用这个的还是比较多的。
            * uuid.uuid4()
            * 如果要去除- .hex即可
        * uuid5()：这个看起来和uuid3()貌似并没有什么不同，写法一样，也是由用户来指定namespace和字符串，不过这里用的散列并不是MD5，而是SHA1.
            * uuid.uuid5(uuid.NAMESPACE_DNS, 'yuanlin')