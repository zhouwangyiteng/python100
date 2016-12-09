# coding: utf-8

import requests
from bs4 import BeautifulSoup
import time


def download(date, header, pageno, grade):
    data['pageno'] = pageno
    data['grade'] = grade
    response = requests.post(request_url, data=data, headers=header)
    soup = BeautifulSoup(response.text)
    hospital_list = soup.find_all(name='tr', attrs={'bgcolor': "#FFFFFF"})
    for each_tr in hospital_list:
        record = []
        for each_td in each_tr.find_all(name='td'):
            record.append(each_td.string)
        record = [i.strip() for i in record[:-1]]+[str(grade)]
        records = ','.join(record).encode('GBK')+'\n'
        print records.decode('GBK')
        with open('records.csv', 'a+') as f:
            f.write(records)

data = {'pageno': '3',
        'qxcode': '',
        'grade': '1',
        'disease': '',
        'speciality': '',
        'unitname': '',
        'address': ''}

header = {'Host': '202.96.245.182',
          'Connection': 'keep-alive',
          'Content - Length': '64',
          'Cache - Control': 'max-age=0',
          'Origin': 'http://202.96.245.182',
          'Upgrade - Insecure - Requests': '1',
          'User - Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
          'Content - Type': 'application/x-www-form-urlencoded',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Referer': 'http://202.96.245.182/xxcx/ddyy.jsp',
          'Accept - Encoding': 'gzip, deflate',
          'Accept - Language': 'en-US,en;q=0.8',
          'Cookie': 'JSESSIONID=0000RakNX6qp3N-3cINVV2M4eun:-1; __utmt=1; __utma=34500258.795249466.1481155062.1481273496.1481285596.4; __utmb=34500258.1.10.1481285596; __utmc=34500258; __utmz=34500258.1481273496.3.3.utmcsr=shyb.gov.cn|utmccn=(referral)|utmcmd=referral|utmcct=/xxcx/yb04.html'
          }

request_url = 'http://202.96.245.182/xxcx/ddyy.jsp'
pages = [114, 23, 8]
grades = [1, 2, 3]

for i in range(3):
    for pageno in range(1, 1+pages[i]):
        print pageno, grades[i]
        download(data, header, pageno, grades[i])
        time.sleep(1)
