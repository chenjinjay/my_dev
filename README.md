# my_dev

# 一、auth.py ：

用python调用zabbix官方文档给的api接口获取zabbix的数据，代码已经有注释，不再说明。


主要参考自： https://www.zabbix.com/documentation/3.0/manual/api/reference/hostgroup/get   只是把该博主的2个函数进行了整合，做成一个函数

zabbix3.0官方文档的API接口： https://www.zabbix.com/documentation/3.0/manual/api
下图为API接口的查找方式

![image](https://github.com/chenjinjay/my_dev/blob/master/picture/1.jpg)

下图为接口示例：

![image](https://github.com/chenjinjay/my_dev/blob/master/picture/2.jpg)

个人总结：

由于还未深入学习这类性质的代码，所以只能根据本次实验总结出一些个人的观点供参考。

个人觉得，应该就是利用get（也可能是post）发送请求，接收返回的结果，两者都用json进行格式处理。作为想向开发发展的纯小白，仿佛打开了新世界的大门，再继续摸索吧，路漫漫...
