import chardet,execjs,json,re

if __name__ == '__main__':
    abc = b"var VideoListJson=[['\xc6\xd5\xcd\xa8\xca\xd3\xc6\xb5',['\\u7B2C01\\u96C6$https://iqiyi.com-t-iqiyi.com/share/5fc34ed307aac159a30d81181c99847e$swf','\\u7B2C02\\u96C6$https://iqiyi.com-t-iqiyi.com/share/acc21473c4525b922286130ffbfe00b5$swf','\\u7B2C03\\u96C6$https://youku.com-ok-pptv.com/share/0b7a9d54deeb611edc4540d286e9a042$swf','\\u7B2C04\\u96C6$https://youku.com-ok-pptv.com/share/94739e5a5164b4d2396e253a11d57044$swf','\\u7B2C05\\u96C6$https://youku.com-ok-pptv.com/share/2adcfc3929e7c03fac3100d3ad51da26$swf','\\u7B2C06\\u96C6$https://youku.com-ok-pptv.com/share/8c66bb19847dd8c21413c5c8c9d68306$swf','\\u7B2C07\\u96C6$https://youku.com-ok-pptv.com/share/c7b03782920d35145eb4c97556d194a3$swf']],['\xb8\xdf\xc7\xe5\xca\xd3\xc6\xb5',['\\u7B2C1\\u96C6$https://cn3.ruioushang.com/hls/20190812/359cedab3c91beb1c823bd185981f2a6/1565588492/index.m3u8$lsyp','\\u7B2C2\\u96C6$https://cn6.merrytime.cc/hls/20190819/939c312ac9cecd42bf816ef2ad368aca/1566178637/index.m3u8$lsyp','\\u7B2C3\\u96C6$https://cn2.microcloud.cc/hls/20190827/05f42626b7a1e5ddbd1dfe640391a927/1566898868/index.m3u8$lsyp','\\u7B2C4\\u96C6$https://cn4.download05.com/hls/20190901/8753b26e2e5a345df5ba8ab2a2f44e60/1567349599/index.m3u8$lsyp','\\u7B2C5\\u96C6$https://cn3.download05.com/hls/20190908/1a69c5a816ad52035a8ca5e79821ec09/1567947040/index.m3u8$lsyp','\\u7B2C6\\u96C6$https://cn2.microcloud.cc/hls/20190915/e7c4a78691ed0a8ea6bc89ae41283615/1568547005/index.m3u8$lsyp','\\u7B2C7\\u96C6$https://www.7639616.com/hls/20190922/cffd21e6b14a35c97189fc4ac1e702ba/1569140768/index.m3u8$lsyp']]],urlinfo='http://'+document.domain+'/OMJ/63852/63852-<from>-<pos>.html';"
    abc = abc.decode('gb2312')
    abc = abc.replace("'+document.domain+'",'')
    ctx = execjs.compile(abc)
    video_list_json = ctx.eval('VideoListJson')
    print(type(video_list_json))
    for vitem in video_list_json:
        name = ''
        dict_list = []
        for v in vitem:
            if type(v) == str:
                name = v
            if type(v) == list:
                for x in v:
                    y = x.split('$')
                    test_dict = {
                        'resouseName': name +',' + y[0],
                        'resouseUrl': y[1],
                        'realPlayUrl': y[1]
                    }
                    dict_list.append(test_dict)
        print(dict_list)


