import json
import re
import requests
import pymysql
import time

wrong_users = []


def ErrorLog(msg):
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    with open('日志输出路径/log.txt', mode='a') as f:
        f.write('--- {} --- {}\n'.format(now, msg))
        f.close()


try:
    # Connect MySQL
    connection = pymysql.connect(host='47.108.208.140', user='root', passwd='2Z4hRbf4BwMyjWMC',
                                 port=3306, db='yiqing', charset='utf8')
    cursor = connection.cursor()

    # Get user and password
    cursor.execute('select * from yiqing')
    user_information = cursor.fetchall()

    # Disconnect MySQL
    connection.commit()
    cursor.close()
    connection.close()
except:
    ErrorLog('Error---MySQL')

try:
    # Request with information collected from MySQL
    for user_data in user_information:
        # Information
        username = user_data[1]
        password = user_data[2]

        # Origin Headers
        headers_session = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'yiqing.ctgu.edu.cn',
            'Referer': 'http://yiqing.ctgu.edu.cn/wx/index/main.do?currSchool=ctgu&CURRENT_YEAR=2019&showWjdc=false&studentShowWjdc=false',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        }

        # 获取服务器端 JSESSIONID
        session_url = 'http://yiqing.ctgu.edu.cn/wx/health/main.do'
        response_session = requests.get(url=session_url, headers=headers_session, allow_redirects=False)
        cookie = re.findall('JSESSIONID=(.*?);', response_session.headers['Set-Cookie'])[0]

        # Headers that with JSESSIONID
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': f'JSESSIONID={cookie}',
            'Host': 'yiqing.ctgu.edu.cn',
            'Origin': 'http://yiqing.ctgu.edu.cn',
            'Referer': 'http://yiqing.ctgu.edu.cn/wx/health/toApply.do',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43',
        }

        # post data
        data = {
            'username': username,
            'password': password,
        }

        # 模拟登录请求，进行 JSESSIONID 账号配对
        login_url = 'http://yiqing.ctgu.edu.cn/wx/index/loginSubmit.do'
        response_data = requests.post(url=login_url, headers=headers, data=data).text

        # 判断账号密码是否正确
        if response_data == 'success':
            # Get token
            apply_url = 'http://yiqing.ctgu.edu.cn/wx/health/toApply.do'
            apply_response = requests.get(url=apply_url, headers=headers).text

            # 判断是否已提交请求
            if re.findall('<input type="hidden" name="ttoken" value="(.*?)"/>', apply_response):
                token = re.findall('<input type="hidden" name="ttoken" value="(.*?)"/>', apply_response)[0]

                # Get last submission data
                before_url = 'http://yiqing.ctgu.edu.cn/wx/health/studentHis.do'
                before_data = requests.post(url=before_url, headers=headers, data=data).text
                before_data_json = json.loads(before_data)

                # 构造提交参数
                data_submit = {
                    'ttoken': token,
                    'province': before_data_json[0]['province'],
                    'city': before_data_json[0]['city'],
                    'district': before_data_json[0]['district'],
                    'adcode': before_data_json[0]['adcode'],
                    'longitude': before_data_json[0]['longitude'],
                    'latitude': before_data_json[0]['latitude'],
                    'sfqz': before_data_json[0]['sfqz'],
                    'sfys': before_data_json[0]['sfys'],
                    'sfzy': before_data_json[0]['sfzy'],
                    'sfgl': before_data_json[0]['sfgl'],
                    'status': before_data_json[0]['status'],
                    'szdz': before_data_json[0]['szdz'],
                    'sjh': before_data_json[0]['sjh'],
                    'lxrxm': before_data_json[0]['lxrxm'],
                    'lxrsjh': before_data_json[0]['lxrsjh'],
                    'sffr': before_data_json[0]['sffr'],
                    'sffrAm': before_data_json[0]['sffrAm'],
                    'sffrNoon': before_data_json[0]['sffrNoon'],
                    'sffrPm': before_data_json[0]['sffrPm'],
                    'sffy': before_data_json[0]['sffy'],
                    'sfgr': before_data_json[0]['sfgr'],
                    'qzglsj': before_data_json[0]['qzglsj'],
                    'qzgldd': before_data_json[0]['qzgldd'],
                    'glyy': before_data_json[0]['glyy'],
                    'mqzz': before_data_json[0]['mqzz'],
                    'sffx': before_data_json[0]['sffx'],
                    'qt': before_data_json[0]['qt'],
                }

                # Final Submit API
                url = 'http://yiqing.ctgu.edu.cn/wx/health/saveApply.do'
                submit = requests.post(url=url, headers=headers, data=data_submit).text
                submit_json = json.loads(submit)
                # ErrorLog(submit_json['msgStatus'])

                time.sleep(1)
            else:
                # ErrorLog('Already Submitted')
                time.sleep(1)

        elif response_data == 'fail':
            wrong_users.append(username)
            # ErrorLog('Wrong User Or Password')
            time.sleep(1)
except:
    ErrorLog('Error---Requests')

# 删除账号密码不正确的用户
if wrong_users:
    try:
        # Connect MySQL
        connection = pymysql.connect(host='127.0.0.1', user='数据库账号', passwd='数据库密码',
                                     port=3306, db='数据库名称', charset='utf8')
        cursor = connection.cursor()

        # Get user and password
        cursor.execute('select * from yiqing')
        user_information = cursor.fetchall()

        for wrong_user in wrong_users:
            cursor.execute('delete from yiqing where user = %s;' % wrong_user)

        # Disconnect MySQL
        connection.commit()
        cursor.close()
        connection.close()

    except:
        ErrorLog('Error---MySQL')

ErrorLog('Finish\n')

