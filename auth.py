#/usr/bin/env python
#coding=utf-8
import json
import urllib2
url = "http://192.168.2.230/zabbix/api_jsonrpc.php"             # 替换成你自己的ip跟端口
header = {
    "Content-Type": "application/json"
}

def auth_login():                      # 获取自动登录的id,每次执行该函数得到的id都是不一样的
    Data = json.dumps(                 # 官方文档提供的api接口 
    {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "Admin",
            "password": "zabbix"
        },
        "id": 1,
    })

    request = urllib2.Request(url,data=Data)
    for key in header:
        request.add_header(key,header[key])     # 加header,一般是反防爬虫，这里应该是确定 HTTP Body 中的内容该怎样解析
    try:
        result = urllib2.urlopen(request)
    except URLError as e:
        print "Auth Failed, Please Check Your Name AndPassword:",e.code
    else:
        response = json.loads(result.read())
        result.close()
        authid = response['result']
        return authid

# A=auth_login()
# print A

def get_data():                                    # 查数据的函数
    authid = auth_login()
    data = json.dumps(                             # 官方给的接口
    {
        "jsonrpc": "2.0",
        "method": "hostgroup.get",                  # 关键字，与output一起决定返回的是什么信息
        "params": {
            "output": ["groupid","name"]
        },
        "auth": authid,
        "id": 1,
    })
    get_request = urllib2.Request(url,data)
    for key in header:
        get_request.add_header(key,header[key])
    try:
        get_result = urllib2.urlopen(get_request)
    except URLError as e:                                    # hasattr 判断返回的信息是否含 'reason' 这个字符串
        if hasattr(e,'reason'):
            print 'We failed to reach a server.'
            print 'Reason:',e.reason
        elif hasattr(e,'code'):
            print 'The server could not fulfill the request.'
            print 'Error code: ', e.code
    else:
        get_response = json.loads(get_result.read())
        get_result.close()
        print "Number Of Hosts: ", len(get_response['result'])
        for group in get_response['result']:
            print "Group ID:",group['groupid'],"\tGroupName:",group['name']

if __name__ == '__main__':
    get_data() 




