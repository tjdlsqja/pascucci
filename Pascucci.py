from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def Pascucci_store(result):
    for page_idx in range(0,54):
        Pascucci_url = 'https://www.caffe-pascucci.co.kr/store/storeList.asp?page=%s' % str(page_idx + 1)
        print(Pascucci_url)
        html = urllib.request.urlopen(Pascucci_url)
        soupPascucci = BeautifulSoup(html, 'html.parser')
        tag_tbody = soupPascucci.find('tbody')
        for store in tag_tbody.find_all('tr'):

            store_td = store.find_all('td')
            store_name = store_td[1].string
            store_address_list = list(store_td[4])
            store_address = store_address_list[1].string
            store_phone_list = list(store_td[5])
            store_phone = store_phone_list[1].string
            result.append([store_name]+[store_address]+[store_phone])

    return

def main():
    result = []
    print('Pascucci store crawling >>>>>>>>>>>>>>>>>>>>>>>>>')
    Pascucci_store(result)
    Pascucci_tbl = pd.DataFrame(result, columns = ('store', 'address', 'phone'))
    Pascucci_tbl.to_csv('D:/pascucci2.csv', encoding = 'cp949', mode = 'w', index = True)
    del result[:]



if __name__ == '__main__':
    main() 




    
        
