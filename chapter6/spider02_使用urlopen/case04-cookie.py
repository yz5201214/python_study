'''
cookie的使用
案例访问我自己的斗鱼关注页面

https://www.douyu.com/directory/myFollow
下面是请求的hearders信息
:authority: www.douyu.com
:method: GET
:path: /directory/myFollow
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: max-age=0
cookie: dy_did=139c9828b9ebd4fe6f0e766c00011501; acf_did=139c9828b9ebd4fe6f0e766c00011501; smidV2=20180627205418e4bcaf20905583eef1b6b60d89afda60009e29d56bcb84df0; _ga=GA1.2.527244826.1540484606; acf_uid=549794; acf_username=auto_ZtAj6gv8So; acf_nickname=%E7%9F%B3%E5%A4%B4%E7%9F%B3%E5%A4%B4; acf_ltkid=87200321; acf_auth=cb9354irKd747SMRPa1YbcMRpTRgc3AWrGKCXRI3FTusOEbR23tkRh3f%2BPQudyDlbb5yML9Z91Qe2YheqrD2A28Uu0JvmyKW3ahr%2BkOyb7mu%2BPW6mqG5T6C9RZE; wan_auth37wan=be8d773b38b5amUZdjAmlhNnKotkmobFZDCJ5aPaKL%2FNG6raO3ZVHVbxx26shCsvSNE0GDOurkp2fM7BkZ51sddhJoqm2Re9yWnMIvwnbhrP2Ic; acf_own_room=0; acf_groupid=1; acf_phonestatus=1; acf_ct=0; acf_biz=1; acf_stk=22da474a42618282; acf_avatar=//apic.douyucdn.cn/upload/avatar/000/54/97/94_avatar_; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1562137614,1562298833,1562724132,1562762936; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1562762951
referer: https://www.douyu.com/directory/myFollow
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
'''
import brotli
from urllib import parse
import requests
from requests.exceptions import RequestException
import gzip
def douyuMyFollow():
    url = 'https://www.douyu.com/member/cp'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    abc = {
        'Cookie': 'dy_did=139c9828b9ebd4fe6f0e766c00011501; acf_did=139c9828b9ebd4fe6f0e766c00011501; smidV2=20180627205418e4bcaf20905583eef1b6b60d89afda60009e29d56bcb84df0; _ga=GA1.2.527244826.1540484606; acf_uid=549794; acf_username=auto_ZtAj6gv8So; acf_nickname=%E7%9F%B3%E5%A4%B4%E7%9F%B3%E5%A4%B4; acf_ltkid=87200321; acf_auth=cb9354irKd747SMRPa1YbcMRpTRgc3AWrGKCXRI3FTusOEbR23tkRh3f%2BPQudyDlbb5yML9Z91Qe2YheqrD2A28Uu0JvmyKW3ahr%2BkOyb7mu%2BPW6mqG5T6C9RZE; wan_auth37wan=be8d773b38b5amUZdjAmlhNnKotkmobFZDCJ5aPaKL%2FNG6raO3ZVHVbxx26shCsvSNE0GDOurkp2fM7BkZ51sddhJoqm2Re9yWnMIvwnbhrP2Ic; acf_own_room=0; acf_groupid=1; acf_phonestatus=1; acf_ct=0; acf_biz=1; acf_stk=22da474a42618282; acf_avatar=//apic.douyucdn.cn/upload/avatar/000/54/97/94_avatar_; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1562137614,1562298833,1562724132,1562762936; PHPSESSID=mrpdhdkif47qhtckgjq24kov93; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1562768293'
    }
    try:
        r = requests.get(url,headers=headers,cookies=abc)
        if r.status_code == 200:
            # 返回的内容是数据流格式，需要转码
            data = r.content.decode('utf-8')
            print(data)
        # req = request.Request(url=url,headers=hearders)
        # response = request.urlopen(req)
        # if response.getcode() == 200:
        #     if response.info()['Content-Encoding'] =='gzip':
        #         with gzip.open(response.read().decode('utf-8','ignore'), 'rb') as f:
        #             file_content = f.read()

    except RequestException as e:
        print(e)

if __name__ == '__main__':
    douyuMyFollow()
