import datetime
import os
import time

import requests

logFile = open(os.getcwd() + '\loginLog.txt', 'a', encoding='utf-8')


def post_request(username: str, passwd: str):
    url = 'http://172.20.20.1:801/srun_portal_pc.php?ac_id=3&'
    s = requests.session()
    headers = {
        'Host': '172.20.20.1:801',
        'Origin': 'http://172.20.20.1:801',
        'Referer': 'http://172.20.20.1:801/srun_portal_pc.php?ac_id=3&',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    post_data = {
        'action': 'login',
        'ac_id': '3',
        'user_ip': '',
        'nas_ip': '',
        'url': '',
        'username': username,
        'password': passwd,
        'save_me': '1'
    }
    # 没有卵用的cookie
    # s.cookies.set('login','')
    s.headers.update(headers)
    status = s.post(url=url, data=post_data).status_code
    if status == 200:
        writeLog('[SUCCESS] login successfully!')


def writeLog(info: str):
    logFile.write(str(datetime.datetime.now())[0:-2] + '\t' + info + '\n')


if __name__ == '__main__':
    for i in range(3):
        try:
            g = requests.get(url='http://172.20.20.1:801/srun_portal_pc.php?ac_id=3&')
            if g.status_code == 200:
                writeLog('[SUCCESS] initialize successfully!')
                break
            else:
                print('Error!' + str(g.status_code))
                writeLog('Error!' + str(g.status_code))
        except Exception as e:
            print(e)
            writeLog('Error!' + e.__str__())
            time.sleep(3)
    else:
        raise e
    post_request('[student ID]', '[campus network password]')
